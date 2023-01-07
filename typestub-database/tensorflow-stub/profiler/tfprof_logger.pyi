from tensorflow.core.profiler import tfprof_log_pb2 as tfprof_log_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.profiler.internal import flops_registry as flops_registry
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

TRAINABLE_VARIABLES: str
REGISTERED_FLOP_STATS: str

def merge_default_with_oplog(graph, op_log: Any | None = ..., run_meta: Any | None = ..., add_trace: bool = ..., add_trainable_var: bool = ...): ...
def write_op_log(graph, log_dir, op_log: Any | None = ..., run_meta: Any | None = ..., add_trace: bool = ...) -> None: ...
