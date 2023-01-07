from tensorflow.python import tf2 as tf2
from tensorflow.python.client import session as session
from tensorflow.python.framework import composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_ragged_conversion_ops as gen_ragged_conversion_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_config as ragged_config, ragged_tensor_value as ragged_tensor_value, ragged_util as ragged_util
from tensorflow.python.ops.ragged.row_partition import RowPartition as RowPartition
from tensorflow.python.types import internal as internal_types
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Any

class RaggedTensor(composite_tensor.CompositeTensor, internal_types.NativeObject):
    def __init__(self, values, row_partition, internal: bool = ...) -> None: ...
    @classmethod
    def from_value_rowids(cls, values, value_rowids, nrows: Any | None = ..., name: Any | None = ..., validate: bool = ...): ...
    @classmethod
    def from_row_splits(cls, values, row_splits, name: Any | None = ..., validate: bool = ...): ...
    @classmethod
    def from_row_lengths(cls, values, row_lengths, name: Any | None = ..., validate: bool = ...): ...
    @classmethod
    def from_row_starts(cls, values, row_starts, name: Any | None = ..., validate: bool = ...): ...
    @classmethod
    def from_row_limits(cls, values, row_limits, name: Any | None = ..., validate: bool = ...): ...
    @classmethod
    def from_uniform_row_length(cls, values, uniform_row_length, nrows: Any | None = ..., validate: bool = ..., name: Any | None = ...): ...
    @classmethod
    def from_nested_value_rowids(cls, flat_values, nested_value_rowids, nested_nrows: Any | None = ..., name: Any | None = ..., validate: bool = ...): ...
    @classmethod
    def from_nested_row_splits(cls, flat_values, nested_row_splits, name: Any | None = ..., validate: bool = ...): ...
    @classmethod
    def from_nested_row_lengths(cls, flat_values, nested_row_lengths, name: Any | None = ..., validate: bool = ...): ...
    @property
    def dtype(self): ...
    @property
    def shape(self): ...
    def get_shape(self): ...
    @property
    def ragged_rank(self): ...
    @property
    def values(self): ...
    @property
    def row_splits(self): ...
    @property
    def uniform_row_length(self): ...
    @property
    def flat_values(self): ...
    @property
    def nested_row_splits(self): ...
    def value_rowids(self, name: Any | None = ...): ...
    def nested_value_rowids(self, name: Any | None = ...): ...
    def nrows(self, out_type: Any | None = ..., name: Any | None = ...): ...
    def row_starts(self, name: Any | None = ...): ...
    def row_limits(self, name: Any | None = ...): ...
    def row_lengths(self, axis: int = ..., name: Any | None = ...): ...
    def nested_row_lengths(self, name: Any | None = ...): ...
    def bounding_shape(self, axis: Any | None = ..., name: Any | None = ..., out_type: Any | None = ...): ...
    def with_values(self, new_values): ...
    def with_flat_values(self, new_values): ...
    def with_row_splits_dtype(self, dtype): ...
    def merge_dims(self, outer_axis, inner_axis): ...
    @classmethod
    def from_tensor(cls, tensor, lengths: Any | None = ..., padding: Any | None = ..., ragged_rank: int = ..., name: Any | None = ..., row_splits_dtype=...): ...
    def to_tensor(self, default_value: Any | None = ..., name: Any | None = ..., shape: Any | None = ...): ...
    @classmethod
    def from_sparse(cls, st_input, name: Any | None = ..., row_splits_dtype=...): ...
    def to_sparse(self, name: Any | None = ...): ...
    def numpy(self): ...
    def to_list(self): ...
    __getitem__: Any
    __ge__: Any
    __gt__: Any
    __le__: Any
    __lt__: Any
    __and__: Any
    __rand__: Any
    __invert__: Any
    __ror__: Any
    __or__: Any
    __xor__: Any
    __rxor__: Any
    __abs__: Any
    __add__: Any
    __radd__: Any
    __div__: Any
    __rdiv__: Any
    __floordiv__: Any
    __rfloordiv__: Any
    __mod__: Any
    __rmod__: Any
    __mul__: Any
    __rmul__: Any
    __neg__: Any
    __pow__: Any
    __rpow__: Any
    __sub__: Any
    __rsub__: Any
    __truediv__: Any
    __rtruediv__: Any
    def consumers(self): ...

def is_ragged(value): ...
def match_row_splits_dtypes(*tensors, **kwargs): ...

class RaggedTensorSpec(type_spec.BatchableTypeSpec):
    @property
    def dtype(self): ...
    @property
    def shape(self): ...
    @property
    def ragged_rank(self): ...
    @property
    def row_splits_dtype(self): ...
    @property
    def flat_values_spec(self): ...
    @property
    def value_type(self): ...
    def __init__(self, shape: Any | None = ..., dtype=..., ragged_rank: Any | None = ..., row_splits_dtype=..., flat_values_spec: Any | None = ...) -> None: ...
    def is_compatible_with(self, spec_or_value): ...
    @classmethod
    def from_value(cls, value): ...

def convert_to_tensor_or_ragged_tensor(value, dtype: Any | None = ..., preferred_dtype: Any | None = ..., name: Any | None = ...): ...

class RaggedTensorType:
    def __init__(self, dtype, ragged_rank, row_splits_dtype=...) -> None: ...
    dtype: Any
    ragged_rank: Any
    row_splits_dtype: Any

def merge_dims(value, outer_axis, inner_axis): ...

Ragged: Any
RaggedOrDense: Any
