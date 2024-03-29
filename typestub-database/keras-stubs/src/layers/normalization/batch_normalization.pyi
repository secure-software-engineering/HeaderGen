from typing import Any

from keras import backend as backend
from keras import constraints as constraints
from keras import initializers as initializers
from keras import regularizers as regularizers
from keras.src.engine.base_layer import Layer as Layer
from keras.src.engine.input_spec import InputSpec as InputSpec
from keras.utils import control_flow_util as control_flow_util

class BatchNormalizationBase(Layer):
    axis: Any
    momentum: Any
    epsilon: Any
    center: Any
    scale: Any
    beta_initializer: Any
    gamma_initializer: Any
    moving_mean_initializer: Any
    moving_variance_initializer: Any
    beta_regularizer: Any
    gamma_regularizer: Any
    beta_constraint: Any
    gamma_constraint: Any
    renorm: Any
    virtual_batch_size: Any
    adjustment: Any
    supports_masking: bool
    fused: Any
    renorm_clipping: Any
    renorm_momentum: Any
    def __init__(
        self,
        axis: int = ...,
        momentum: float = ...,
        epsilon: float = ...,
        center: bool = ...,
        scale: bool = ...,
        beta_initializer: str = ...,
        gamma_initializer: str = ...,
        moving_mean_initializer: str = ...,
        moving_variance_initializer: str = ...,
        beta_regularizer: Any | None = ...,
        gamma_regularizer: Any | None = ...,
        beta_constraint: Any | None = ...,
        gamma_constraint: Any | None = ...,
        renorm: bool = ...,
        renorm_clipping: Any | None = ...,
        renorm_momentum: float = ...,
        fused: Any | None = ...,
        trainable: bool = ...,
        virtual_batch_size: Any | None = ...,
        adjustment: Any | None = ...,
        name: Any | None = ...,
        **kwargs
    ) -> None: ...
    @property
    def trainable(self): ...
    @trainable.setter
    def trainable(self, value) -> None: ...
    input_spec: Any
    gamma: Any
    beta: Any
    moving_mean: Any
    moving_variance: Any
    moving_stddev: Any
    renorm_mean: Any
    renorm_stddev: Any
    built: bool
    def build(self, input_shape): ...
    def call(self, inputs, training: Any | None = ...): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class SyncBatchNormalization(BatchNormalizationBase):
    def __init__(
        self,
        axis: int = ...,
        momentum: float = ...,
        epsilon: float = ...,
        center: bool = ...,
        scale: bool = ...,
        beta_initializer: str = ...,
        gamma_initializer: str = ...,
        moving_mean_initializer: str = ...,
        moving_variance_initializer: str = ...,
        beta_regularizer: Any | None = ...,
        gamma_regularizer: Any | None = ...,
        beta_constraint: Any | None = ...,
        gamma_constraint: Any | None = ...,
        **kwargs
    ) -> None: ...

class BatchNormalization(BatchNormalizationBase):
    def __init__(
        self,
        axis: int = ...,
        momentum: float = ...,
        epsilon: float = ...,
        center: bool = ...,
        scale: bool = ...,
        beta_initializer: str = ...,
        gamma_initializer: str = ...,
        moving_mean_initializer: str = ...,
        moving_variance_initializer: str = ...,
        beta_regularizer: Any | None = ...,
        gamma_regularizer: Any | None = ...,
        beta_constraint: Any | None = ...,
        gamma_constraint: Any | None = ...,
        **kwargs
    ) -> None: ...
