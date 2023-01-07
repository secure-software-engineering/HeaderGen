from tensorflow.python.framework import ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.keras.utils import tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, lookup_ops as lookup_ops, math_ops as math_ops, string_ops as string_ops
from tensorflow.python.ops.ragged import ragged_functional_ops as ragged_functional_ops, ragged_tensor as ragged_tensor, ragged_tensor_value as ragged_tensor_value
from tensorflow.python.platform import gfile as gfile
from typing import Any

class TableHandler:
    table: Any
    mutable: Any
    mask_token: Any
    mask_value: Any
    oov_tokens: Any
    def __init__(self, table, oov_tokens: Any | None = ..., mask_token: Any | None = ..., mask_value: int = ...) -> None: ...
    def table_size(self): ...
    def clear(self): ...
    def insert(self, keys, values) -> None: ...
    def lookup(self, inputs): ...

def num_tokens_in_file(vocabulary_path): ...
def get_vocabulary_from_file(vocabulary_path, encoding: str = ...): ...
def find_repeated_tokens(vocabulary): ...
