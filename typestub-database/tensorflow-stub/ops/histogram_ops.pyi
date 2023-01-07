from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, clip_ops as clip_ops, gen_math_ops as gen_math_ops, math_ops as math_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def histogram_fixed_width_bins(values, value_range, nbins: int = ..., dtype=..., name: Any | None = ...): ...
def histogram_fixed_width(values, value_range, nbins: int = ..., dtype=..., name: Any | None = ...): ...
