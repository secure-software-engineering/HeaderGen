import enum
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, immutable_dict as immutable_dict, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util import type_annotations as type_annotations
from typing import Any

RESERVED_FIELD_NAMES: Any

class Sentinel:
    def __init__(self, name) -> None: ...

class ExtensionTypeField:
    NO_DEFAULT: Any
    def __new__(cls, name, value_type, default=...): ...
    @staticmethod
    def is_reserved_name(name): ...

def validate_field_value_type(value_type, in_mapping_key: bool = ..., allow_forward_references: bool = ...) -> None: ...

class _ConversionContext(enum.Enum):
    VALUE: int
    SPEC: int
    DEFAULT: int

def convert_fields(fields, field_values) -> None: ...
def convert_fields_for_spec(fields, field_values) -> None: ...
