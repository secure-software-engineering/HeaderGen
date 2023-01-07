from tensorflow.core.protobuf import config_pb2 as config_pb2, meta_graph_pb2 as meta_graph_pb2
from tensorflow.python.client import session as session
from tensorflow.python.framework import graph_util as graph_util, tensor_shape as tensor_shape, versions as versions
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.platform import test as test

def aot_compile_cpu_meta_graph_def(checkpoint_path, meta_graph_def, output_prefix, signature_def_key, cpp_class, target_triple, target_cpu, variables_to_feed=..., multithreading: bool = ...) -> None: ...
