from tensorflow.python.framework import ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import control_flow_ops as control_flow_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def smart_cond(pred, true_fn: Any | None = ..., false_fn: Any | None = ..., name: Any | None = ...): ...
def smart_constant_value(pred): ...
def smart_case(pred_fn_pairs, default: Any | None = ..., exclusive: bool = ..., name: str = ...): ...
