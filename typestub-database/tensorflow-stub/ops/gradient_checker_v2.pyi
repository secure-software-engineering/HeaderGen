from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def compute_gradient(f, x, delta: Any | None = ...): ...
def max_error(grad1, grad2): ...
