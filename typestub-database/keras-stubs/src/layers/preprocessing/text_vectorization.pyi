from typing import Any

from keras import backend as backend
from keras.src.engine import base_preprocessing_layer as base_preprocessing_layer
from keras.src.layers.preprocessing import string_lookup as string_lookup
from keras.src.saving.saved_model import layer_serialization as layer_serialization
from keras.utils import layer_utils as layer_utils
from keras.utils import tf_utils as tf_utils

LOWER_AND_STRIP_PUNCTUATION: str
STRIP_PUNCTUATION: str
LOWER: str
WHITESPACE: str
CHARACTER: str
TF_IDF: Any
INT: Any
MULTI_HOT: Any
COUNT: Any
DEFAULT_STRIP_REGEX: str

class TextVectorization(base_preprocessing_layer.PreprocessingLayer):
    def __init__(
        self,
        max_tokens: Any | None = ...,
        standardize: str = ...,
        split: str = ...,
        ngrams: Any | None = ...,
        output_mode: str = ...,
        output_sequence_length: Any | None = ...,
        pad_to_max_tokens: bool = ...,
        vocabulary: Any | None = ...,
        idf_weights: Any | None = ...,
        sparse: bool = ...,
        ragged: bool = ...,
        **kwargs
    ) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def adapt(
        self, data, batch_size: Any | None = ..., steps: Any | None = ...
    ) -> None: ...
    def update_state(self, data) -> None: ...
    def finalize_state(self) -> None: ...
    def reset_state(self) -> None: ...
    def get_vocabulary(self, include_special_tokens: bool = ...): ...
    def vocabulary_size(self): ...
    def get_config(self): ...
    def set_vocabulary(self, vocabulary, idf_weights: Any | None = ...) -> None: ...
    def call(self, inputs): ...
