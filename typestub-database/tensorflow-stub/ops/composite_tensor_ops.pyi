from tensorflow.core.protobuf import composite_tensor_variant_pb2 as composite_tensor_variant_pb2
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_composite_tensor_ops as gen_composite_tensor_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import nest as nest
from typing import Any

def composite_tensor_to_variants(value, type_spec: Any | None = ..., name: Any | None = ...): ...
def composite_tensor_from_variant(encoded, type_spec, name: Any | None = ...): ...
