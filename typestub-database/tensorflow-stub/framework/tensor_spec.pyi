from tensorflow.python.framework import common_shapes as common_shapes, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, type_spec as type_spec
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class DenseSpec(type_spec.TypeSpec):
    def __init__(self, shape, dtype=..., name: Any | None = ...) -> None: ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...
    @property
    def name(self): ...
    def is_compatible_with(self, spec_or_value): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def most_specific_compatible_type(self, other): ...

class TensorSpec(DenseSpec, type_spec.BatchableTypeSpec):
    def is_compatible_with(self, spec_or_tensor): ...
    @classmethod
    def from_spec(cls, spec, name: Any | None = ...): ...
    @classmethod
    def from_tensor(cls, tensor, name: Any | None = ...): ...
    @property
    def value_type(self): ...

class BoundedTensorSpec(TensorSpec):
    def __init__(self, shape, dtype, minimum, maximum, name: Any | None = ...) -> None: ...
    @classmethod
    def from_spec(cls, spec): ...
    @property
    def minimum(self): ...
    @property
    def maximum(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __reduce__(self): ...
