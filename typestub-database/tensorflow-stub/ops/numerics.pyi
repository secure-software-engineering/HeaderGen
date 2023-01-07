from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def verify_tensor_all_finite(t: Any | None = ..., msg: Any | None = ..., name: Any | None = ..., x: Any | None = ..., message: Any | None = ...): ...
def verify_tensor_all_finite_v2(x, message, name: Any | None = ...): ...
def add_check_numerics_ops(): ...
