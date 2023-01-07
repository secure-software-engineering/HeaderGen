from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, tensor_pb2 as tensor_pb2, tensor_shape_pb2 as tensor_shape_pb2, types_pb2 as types_pb2
from tensorflow.python.framework import dtypes as dtypes, op_callbacks as op_callbacks, op_def_registry as op_def_registry, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.util import compat as compat, tf_contextlib as tf_contextlib
from typing import Any

def apply_op(op_type_name, name: Any | None = ..., **keywords): ...
def value_to_attr_value(value, attr_type, arg_name): ...
