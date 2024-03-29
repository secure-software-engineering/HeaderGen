from typing import Any

import tensorflow.compat.v2 as tf
from keras import backend as backend
from keras.src.engine import base_layer_utils as base_layer_utils
from keras.src.engine import base_preprocessing_layer as base_preprocessing_layer
from keras.src.saving.saved_model import layer_serialization as layer_serialization
from keras.utils import layer_utils as layer_utils
from keras.utils import tf_utils as tf_utils

INT: Any
MULTI_HOT: Any
ONE_HOT: Any
COUNT: Any
TF_IDF: Any

class NullInitializer(tf.lookup.KeyValueTensorInitializer):
    def __init__(self, key_dtype, value_dtype) -> None: ...
    @property
    def key_dtype(self): ...
    @property
    def value_dtype(self): ...
    def initialize(self, table) -> None: ...

class VocabWeightHandler(base_layer_utils.TrackableWeightHandler):
    def __init__(self, lookup_layer) -> None: ...
    @property
    def num_tensors(self): ...
    def set_weights(self, weights) -> None: ...
    def get_tensors(self): ...

class IndexLookup(base_preprocessing_layer.PreprocessingLayer):
    invert: Any
    max_tokens: Any
    num_oov_indices: Any
    mask_token: Any
    oov_token: Any
    output_mode: Any
    sparse: Any
    pad_to_max_tokens: Any
    vocabulary_dtype: Any
    input_vocabulary: Any
    input_idf_weights: Any
    idf_weights: Any
    idf_weights_const: Any
    lookup_table: Any
    token_counts: Any
    token_document_counts: Any
    num_documents: Any
    def __init__(
        self,
        max_tokens,
        num_oov_indices,
        mask_token,
        oov_token,
        vocabulary_dtype,
        vocabulary: Any | None = ...,
        idf_weights: Any | None = ...,
        invert: bool = ...,
        output_mode: str = ...,
        sparse: bool = ...,
        pad_to_max_tokens: bool = ...,
        **kwargs
    ) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def get_vocabulary(self, include_special_tokens: bool = ...): ...
    def vocabulary_size(self): ...
    def vocab_size(self): ...
    def get_config(self): ...
    def set_vocabulary(self, vocabulary, idf_weights: Any | None = ...) -> None: ...
    def update_state(self, data): ...
    def finalize_state(self) -> None: ...
    def reset_state(self) -> None: ...
    def call(self, inputs): ...
