from typing import Any

from keras import constraints as constraints
from keras import initializers as initializers
from keras import regularizers as regularizers
from keras.src.engine.base_layer import Layer as Layer
from keras.src.layers import advanced_activations as advanced_activations
from keras.src.layers import core as core
from keras.src.layers import einsum_dense as einsum_dense
from keras.utils import tf_utils as tf_utils

class MultiHeadAttention(Layer):
    def __init__(
        self,
        num_heads,
        key_dim,
        value_dim: Any | None = ...,
        dropout: float = ...,
        use_bias: bool = ...,
        output_shape: Any | None = ...,
        attention_axes: Any | None = ...,
        kernel_initializer: str = ...,
        bias_initializer: str = ...,
        kernel_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        activity_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        **kwargs
    ) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
    def call(
        self,
        query,
        value,
        key: Any | None = ...,
        attention_mask: Any | None = ...,
        return_attention_scores: bool = ...,
        training: Any | None = ...,
    ): ...
