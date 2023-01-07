from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.keras.layers.preprocessing import index_lookup as index_lookup, table_utils as table_utils
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class StringLookup(index_lookup.IndexLookup):
    encoding: Any
    def __init__(self, max_tokens: Any | None = ..., num_oov_indices: int = ..., mask_token: Any | None = ..., oov_token: str = ..., vocabulary: Any | None = ..., encoding: Any | None = ..., invert: bool = ..., output_mode=..., sparse: bool = ..., pad_to_max_tokens: bool = ..., **kwargs) -> None: ...
    def get_config(self): ...
    def set_vocabulary(self, vocabulary, idf_weights: Any | None = ...) -> None: ...
