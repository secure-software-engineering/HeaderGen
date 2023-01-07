from keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine import base_layer_utils as base_layer_utils
from keras.engine.base_layer import Layer as Layer
from keras.utils import tf_utils as tf_utils
from typing import Any

class Embedding(Layer):
    input_dim: Any
    output_dim: Any
    embeddings_initializer: Any
    embeddings_regularizer: Any
    activity_regularizer: Any
    embeddings_constraint: Any
    mask_zero: Any
    supports_masking: Any
    input_length: Any
    def __init__(self, input_dim, output_dim, embeddings_initializer: str = ..., embeddings_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., embeddings_constraint: Any | None = ..., mask_zero: bool = ..., input_length: Any | None = ..., **kwargs) -> None: ...
    embeddings: Any
    built: bool
    def build(self, input_shape: Any | None = ...) -> None: ...
    def compute_mask(self, inputs, mask: Any | None = ...): ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...
