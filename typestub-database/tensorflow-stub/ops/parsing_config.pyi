from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops, sparse_ops as sparse_ops
from tensorflow.python.ops.ragged import ragged_math_ops as ragged_math_ops, ragged_tensor as ragged_tensor
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class VarLenFeature: ...

class RaggedFeature:

    class RowSplits(NamedTuple):
        key: Any

    class RowLengths(NamedTuple):
        key: Any

    class RowStarts(NamedTuple):
        key: Any

    class RowLimits(NamedTuple):
        key: Any

    class ValueRowIds(NamedTuple):
        key: Any

    class UniformRowLength(NamedTuple):
        length: Any
    def __new__(cls, dtype, value_key: Any | None = ..., partitions=..., row_splits_dtype=..., validate: bool = ...): ...

class SparseFeature:
    def __new__(cls, index_key, value_key, dtype, size, already_sorted: bool = ...): ...

class FixedLenFeature:
    def __new__(cls, shape, dtype, default_value: Any | None = ...): ...

class FixedLenSequenceFeature:
    def __new__(cls, shape, dtype, allow_missing: bool = ..., default_value: Any | None = ...): ...

class _ParseOpParams:
    sparse_keys: Any
    sparse_types: Any
    dense_keys: Any
    dense_types: Any
    dense_shapes: Any
    dense_defaults: Any
    ragged_keys: Any
    ragged_value_types: Any
    ragged_split_types: Any
    def __init__(self, sparse_keys: Any | None = ..., sparse_types: Any | None = ..., dense_keys: Any | None = ..., dense_types: Any | None = ..., dense_defaults: Any | None = ..., dense_shapes: Any | None = ..., ragged_keys: Any | None = ..., ragged_value_types: Any | None = ..., ragged_split_types: Any | None = ...) -> None: ...
    @classmethod
    def from_features(cls, features, types): ...
    @property
    def dense_shapes_as_proto(self): ...
    @property
    def num_features(self): ...
    @property
    def dense_defaults_vec(self): ...
