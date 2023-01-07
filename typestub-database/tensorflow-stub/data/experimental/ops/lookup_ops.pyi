from tensorflow.python.data.experimental.ops.cardinality import assert_cardinality as assert_cardinality
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import lookup_ops as lookup_ops, math_ops as math_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class DatasetInitializer(lookup_ops.TableInitializerBase):
    dataset: Any
    def __init__(self, dataset) -> None: ...
    def initialize(self, table): ...

def table_from_dataset(dataset: Any | None = ..., num_oov_buckets: int = ..., vocab_size: Any | None = ..., default_value: Any | None = ..., hasher_spec=..., key_dtype=..., name: Any | None = ...): ...
def index_table_from_dataset(dataset: Any | None = ..., num_oov_buckets: int = ..., vocab_size: Any | None = ..., default_value: int = ..., hasher_spec=..., key_dtype=..., name: Any | None = ...): ...
