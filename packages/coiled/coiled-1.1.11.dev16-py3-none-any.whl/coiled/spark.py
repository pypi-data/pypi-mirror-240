"""
Note that pyrightconfig.json is set to ignore this file. If our spark integration becomes more well supported,
we should undo that and fix the type errors.
"""

import asyncio
import multiprocessing
import os
import pathlib
import shlex
import subprocess
import sys

# pyspark isn't a requirement for coiled, but
# maybe we should have some try/except with an explanation
import pyspark  # type: ignore
from dask.distributed import Client
from distributed.diagnostics.plugin import SchedulerPlugin, WorkerPlugin
from pyspark.sql import SparkSession
from urllib3.util import parse_url

from coiled import Cluster

SPARK_CONNECT_PORT = 15003  # this provides ssl termination with proxy in front of 15002
DEBUG_PORTS = [
    22,  # ssh
    7077,  # spark master <-> worker, so usually just internal to cluster
    # dashboards usually get proxied to 443 with auth
    8787,  # dash dashboard
    4040,  # spark connect
    8080,  # spark master
    15002,  # spark gRPC port directly exposed without ssl/bearer auth
]
SPARK_VERSION = pyspark.__version__
# sc._jvm.org.apache.hadoop.util.VersionInfo.getVersion()
HADOOP_AWS_VERSION = "3.3.4"
AWS_JAVA_SDK_BUNDLE_VERSION = "1.12.262"


class SparkMaster(SchedulerPlugin):
    name = "spark-master"
    cls = "org.apache.spark.deploy.master.Master"

    def start(self, scheduler):
        self.scheduler = scheduler
        self.scheduler.add_plugin(self)

        path = pathlib.Path(pyspark.__file__).absolute()
        module_loc = path.parent
        os.environ["SPARK_HOME"] = str(module_loc)
        os.environ["PYSPARK_PYTHON"] = sys.executable

        host = scheduler.address.split("//")[1].split(":")[0]
        cmd = f"spark-class {self.cls} --host {host} --port 7077 --webui-port 8080"
        print(f"Executing\n{cmd}")
        self.proc = subprocess.Popen(shlex.split(cmd))
        print("Launched Spark Master")

    def close(self):
        self.proc.terminate()
        self.proc.wait()
        return super().close()


class SparkConnect(SchedulerPlugin):
    name = "spark-connect"
    cls = "org.apache.spark.sql.connect.service.SparkConnectServer"

    async def start(self, scheduler):
        print("Starting SparkConnect")
        self.scheduler = scheduler
        self.scheduler.add_plugin(self)

        # We need a worker so we know how large to set executors
        while not self.scheduler.workers:
            print("Spark connect waiting for first worker to appear ...")
            await asyncio.sleep(1)

        ws = self.scheduler.workers.values()[0]

        path = pathlib.Path(pyspark.__file__).absolute()
        module_loc = path.parent
        os.environ["SPARK_HOME"] = str(module_loc)
        os.environ["PYSPARK_PYTHON"] = sys.executable

        host = scheduler.address.split("//")[1].split(":")[0]
        spark_master = f"{host}:7077"
        cmd = (
            f"spark-submit --class {self.cls} "
            '--name "SparkConnectServer" '
            f"--packages org.apache.spark:spark-connect_2.12:{pyspark.__version__}"
            f",{','.join(PACKAGES)} "
            f"--master spark://{spark_master} "
            f"--conf spark.driver.host={host} "
            f"--conf spark.executor.memory={ws.memory_limit // 2**30}g "
            f"--conf spark.executor.cores={ws.nthreads} "
            f"--conf spark.hadoop.fs.s3a.aws.credentials.provider="
            "com.amazonaws.auth.EnvironmentVariableCredentialsProvider"
            ",org.apache.hadoop.fs.s3a.auth.IAMInstanceCredentialsProvider"
            ",com.amazonaws.auth.profile.ProfileCredentialsProvider "
        )
        print(f"Executing\n{cmd}")
        self.proc = subprocess.Popen(shlex.split(cmd))

    def close(self):
        self.proc.terminate()
        self.proc.wait()
        return super().close()


class SparkWorker(WorkerPlugin):
    name = "spark-worker"
    cls = "org.apache.spark.deploy.worker.Worker"

    def setup(self, worker):
        self.worker = worker

        path = pathlib.Path(pyspark.__file__).absolute()
        module_loc = path.parent
        os.environ["SPARK_HOME"] = str(module_loc)
        os.environ["PYSPARK_PYTHON"] = sys.executable

        # Sometimes Dask super-saturates cores.  Don't do this for Spark.
        # not sure if this actually has any impact though ...
        cores = min(self.worker.state.nthreads, multiprocessing.cpu_count())

        host = worker.scheduler.address.split("//")[1].split(":")[0]
        spark_master = f"spark://{host}:7077"
        print(f"Launching Spark Worker connecting to {spark_master}")
        cmd = (
            f"spark-class {self.cls} {spark_master} "
            f"--cores {cores} "
            f"--memory {self.worker.memory_manager.memory_limit // 2**30}G "
        )
        self.proc = subprocess.Popen(shlex.split(cmd))
        print("Launched Spark Worker")

    def close(self):
        self.proc.terminate()
        self.proc.wait()
        return super().close()


PACKAGES = (
    f"org.apache.hadoop:hadoop-client:{HADOOP_AWS_VERSION}",
    f"org.apache.hadoop:hadoop-common:{HADOOP_AWS_VERSION}",
    f"org.apache.hadoop:hadoop-aws:{HADOOP_AWS_VERSION}",
    f"com.amazonaws:aws-java-sdk-bundle:{AWS_JAVA_SDK_BUNDLE_VERSION}",
)


def get_spark(client: Client, name="Coiled") -> SparkSession:
    """Launch Spark on a Dask Client

    This returns a ``spark`` session instance connected via SparkConnect
    """
    from coiled.spark import SparkConnect, SparkMaster, SparkWorker

    host = parse_url(client.dashboard_link).host
    token = parse_url(client.dashboard_link).query
    remote_address = f"sc://{host}:{SPARK_CONNECT_PORT}/;use_ssl=true;{token}"

    client.register_plugin(SparkMaster(), idempotent=True)
    client.register_plugin(SparkWorker(), idempotent=True)
    client.register_plugin(SparkConnect(), idempotent=True)

    spark = SparkSession.builder.remote(remote_address).appName(name).getOrCreate()
    return spark


def get_spark_cluster(_open_debug_ports=False, *args, **kwargs):
    cluster = Cluster(
        *args,
        **kwargs,
        backend_options={
            "ingress": [
                {
                    "ports": [443, 8786, SPARK_CONNECT_PORT, *(DEBUG_PORTS if _open_debug_ports else [])],
                    "cidr": "0.0.0.0/0",
                },
            ],
        },
    )
    return cluster
