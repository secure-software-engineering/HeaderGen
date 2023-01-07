from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.distribute.cluster_resolver.tpu_cluster_resolver import TPUClusterResolver as TPUClusterResolver
from tensorflow.python.eager import context as context, function as function
from tensorflow.python.framework import device as device, errors as errors, ops as ops
from tensorflow.python.tpu import topology as topology, tpu as tpu
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def initialize_tpu_system(cluster_resolver: Any | None = ...): ...
def get_initialized_tpu_systems(): ...
def shutdown_tpu_system(cluster_resolver: Any | None = ...) -> None: ...
