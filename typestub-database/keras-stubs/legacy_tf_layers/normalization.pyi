from keras.layers.normalization import batch_normalization_v1 as batch_normalization_v1
from keras.legacy_tf_layers import base as base
from typing import Any

class BatchNormalization(batch_normalization_v1.BatchNormalization, base.Layer):
    def __init__(self, axis: int = ..., momentum: float = ..., epsilon: float = ..., center: bool = ..., scale: bool = ..., beta_initializer=..., gamma_initializer=..., moving_mean_initializer=..., moving_variance_initializer=..., beta_regularizer: Any | None = ..., gamma_regularizer: Any | None = ..., beta_constraint: Any | None = ..., gamma_constraint: Any | None = ..., renorm: bool = ..., renorm_clipping: Any | None = ..., renorm_momentum: float = ..., fused: Any | None = ..., trainable: bool = ..., virtual_batch_size: Any | None = ..., adjustment: Any | None = ..., name: Any | None = ..., **kwargs) -> None: ...
    def call(self, inputs, training: bool = ...): ...

def batch_normalization(inputs, axis: int = ..., momentum: float = ..., epsilon: float = ..., center: bool = ..., scale: bool = ..., beta_initializer=..., gamma_initializer=..., moving_mean_initializer=..., moving_variance_initializer=..., beta_regularizer: Any | None = ..., gamma_regularizer: Any | None = ..., beta_constraint: Any | None = ..., gamma_constraint: Any | None = ..., training: bool = ..., trainable: bool = ..., name: Any | None = ..., reuse: Any | None = ..., renorm: bool = ..., renorm_clipping: Any | None = ..., renorm_momentum: float = ..., fused: Any | None = ..., virtual_batch_size: Any | None = ..., adjustment: Any | None = ...): ...
BatchNorm = BatchNormalization
batch_norm = batch_normalization
