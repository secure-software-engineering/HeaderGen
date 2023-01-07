from tensorflow.core.framework import function_pb2 as function_pb2, op_def_pb2 as op_def_pb2
from tensorflow.python.framework import op_def_registry as op_def_registry
from typing import Any

def graph_to_function_def(graph, operations, inputs, outputs, out_names: Any | None = ...): ...
