from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.python.platform import gfile as gfile, tf_logging as tf_logging
from typing import Any

OPS_WITHOUT_KERNEL_ALLOWLIST: Any
FLEX_PREFIX: bytes
FLEX_PREFIX_LENGTH: Any

def get_ops_and_kernels(proto_fileformat, proto_files, default_ops_str): ...
def get_header_from_ops_and_kernels(ops_and_kernels, include_all_ops_and_kernels): ...
def get_header(graphs, proto_fileformat: str = ..., default_ops: str = ...): ...
