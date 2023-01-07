from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.keras import constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.layers import advanced_activations as advanced_activations, core as core, einsum_dense as einsum_dense
from tensorflow.python.keras.utils import tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, special_math_ops as special_math_ops
from tensorflow.python.util.tf_export import keras_export as keras_export
from typing import Any

class MultiHeadAttention(Layer):
    def __init__(self, num_heads, key_dim, value_dim: Any | None = ..., dropout: float = ..., use_bias: bool = ..., output_shape: Any | None = ..., attention_axes: Any | None = ..., kernel_initializer: str = ..., bias_initializer: str = ..., kernel_regularizer: Any | None = ..., bias_regularizer: Any | None = ..., activity_regularizer: Any | None = ..., kernel_constraint: Any | None = ..., bias_constraint: Any | None = ..., **kwargs) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
    def call(self, query, value, key: Any | None = ..., attention_mask: Any | None = ..., return_attention_scores: bool = ..., training: Any | None = ...): ...
