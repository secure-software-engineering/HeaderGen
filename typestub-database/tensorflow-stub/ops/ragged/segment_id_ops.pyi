from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_util as ragged_util
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def row_splits_to_segment_ids(splits, name: Any | None = ..., out_type: Any | None = ...): ...
def segment_ids_to_row_splits(segment_ids, num_segments: Any | None = ..., out_type: Any | None = ..., name: Any | None = ...): ...
