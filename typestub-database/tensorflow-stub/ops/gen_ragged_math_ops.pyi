from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _RaggedRangeOutput(NamedTuple):
    rt_nested_splits: Any
    rt_dense_values: Any

def ragged_range(starts, limits, deltas, Tsplits=..., name: Any | None = ...): ...

RaggedRange: Any

def ragged_range_eager_fallback(starts, limits, deltas, Tsplits, name, ctx): ...
