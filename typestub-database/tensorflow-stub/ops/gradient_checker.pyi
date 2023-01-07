from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gradients as gradients, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def compute_gradient(x, x_shape, y, y_shape, x_init_value: Any | None = ..., delta: float = ..., init_targets: Any | None = ..., extra_feed_dict: Any | None = ...): ...
def compute_gradient_error(x, x_shape, y, y_shape, x_init_value: Any | None = ..., delta: float = ..., init_targets: Any | None = ..., extra_feed_dict: Any | None = ...): ...
