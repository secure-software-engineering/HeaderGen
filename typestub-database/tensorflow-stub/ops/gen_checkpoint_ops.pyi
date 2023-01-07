from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

class _GenerateVocabRemappingOutput(NamedTuple):
    remapping: Any
    num_present: Any

def generate_vocab_remapping(new_vocab_file, old_vocab_file, new_vocab_offset, num_new_vocab, old_vocab_size: int = ..., name: Any | None = ...): ...

GenerateVocabRemapping: Any

def generate_vocab_remapping_eager_fallback(new_vocab_file, old_vocab_file, new_vocab_offset, num_new_vocab, old_vocab_size, name, ctx): ...
def load_and_remap_matrix(ckpt_path, old_tensor_name, row_remapping, col_remapping, initializing_values, num_rows, num_cols, max_rows_in_memory: int = ..., name: Any | None = ...): ...

LoadAndRemapMatrix: Any

def load_and_remap_matrix_eager_fallback(ckpt_path, old_tensor_name, row_remapping, col_remapping, initializing_values, num_rows, num_cols, max_rows_in_memory, name, ctx): ...
