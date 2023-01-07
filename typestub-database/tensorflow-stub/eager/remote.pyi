from tensorflow.core.protobuf.tensorflow_server_pb2 import ServerDef as ServerDef
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.distribute import device_util as device_util
from tensorflow.python.distribute.cluster_resolver import cluster_resolver as cluster_resolver
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.platform import remote_utils as remote_utils
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def connect_to_remote_host(remote_host: Any | None = ..., job_name: str = ...) -> None: ...
def connect_to_cluster(cluster_spec_or_resolver, job_name: str = ..., task_index: int = ..., protocol: Any | None = ..., make_master_device_default: bool = ..., cluster_device_filters: Any | None = ...) -> None: ...
