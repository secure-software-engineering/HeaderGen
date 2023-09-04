from typing import Any

from keras.src.engine import base_preprocessing_layer as base_preprocessing_layer
from keras.src.layers.preprocessing import index_lookup as index_lookup

class StringLookup(index_lookup.IndexLookup):
    encoding: Any
    def __init__(
        self,
        max_tokens: Any | None = ...,
        num_oov_indices: int = ...,
        mask_token: Any | None = ...,
        oov_token: str = ...,
        vocabulary: Any | None = ...,
        idf_weights: Any | None = ...,
        encoding: Any | None = ...,
        invert: bool = ...,
        output_mode: str = ...,
        sparse: bool = ...,
        pad_to_max_tokens: bool = ...,
        **kwargs
    ) -> None: ...
    def get_config(self): ...
    def adapt(
        self, data, batch_size: Any | None = ..., steps: Any | None = ...
    ) -> None: ...
