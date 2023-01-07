from tensorflow.core.framework import function_pb2 as function_pb2, graph_pb2 as graph_pb2, tensor_shape_pb2 as tensor_shape_pb2, types_pb2 as types_pb2, versions_pb2 as versions_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import cpp_shape_inference_pb2 as cpp_shape_inference_pb2, importer as importer, ops as ops, versions as versions
from tensorflow.python.framework.func_graph import FuncGraph as FuncGraph
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops
from typing import Any

def function_def_to_graph(fdef, input_shapes: Any | None = ...): ...
def is_function(fname): ...
def function_def_to_graph_def(fdef, input_shapes: Any | None = ...): ...
