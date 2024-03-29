from typing import Any, NamedTuple

from keras import activations as activations
from keras import backend as backend
from keras import initializers as initializers
from keras.legacy_tf_layers import base as base_layer
from keras.src.engine import base_layer_utils as base_layer_utils
from keras.src.engine import input_spec as input_spec
from keras.src.layers.legacy_rnn import rnn_cell_wrapper_impl as rnn_cell_wrapper_impl
from keras.utils import tf_utils as tf_utils

ASSERT_LIKE_RNNCELL_ERROR_REGEXP: str

def assert_like_rnncell(cell_name, cell) -> None: ...

class RNNCell(base_layer.Layer):
    def __init__(
        self,
        trainable: bool = ...,
        name: Any | None = ...,
        dtype: Any | None = ...,
        **kwargs
    ) -> None: ...
    def __call__(self, inputs, state, scope: Any | None = ...): ...
    @property
    def state_size(self) -> None: ...
    @property
    def output_size(self) -> None: ...
    def build(self, _) -> None: ...
    def get_initial_state(
        self,
        inputs: Any | None = ...,
        batch_size: Any | None = ...,
        dtype: Any | None = ...,
    ): ...
    def zero_state(self, batch_size, dtype): ...
    def get_config(self): ...

class LayerRNNCell(RNNCell):
    def __call__(self, inputs, state, scope: Any | None = ..., *args, **kwargs): ...

class BasicRNNCell(LayerRNNCell):
    input_spec: Any
    def __init__(
        self,
        num_units,
        activation: Any | None = ...,
        reuse: Any | None = ...,
        name: Any | None = ...,
        dtype: Any | None = ...,
        **kwargs
    ) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def call(self, inputs, state): ...
    def get_config(self): ...

class GRUCell(LayerRNNCell):
    input_spec: Any
    def __init__(
        self,
        num_units,
        activation: Any | None = ...,
        reuse: Any | None = ...,
        kernel_initializer: Any | None = ...,
        bias_initializer: Any | None = ...,
        name: Any | None = ...,
        dtype: Any | None = ...,
        **kwargs
    ) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def call(self, inputs, state): ...
    def get_config(self): ...

class _LSTMStateTuple(NamedTuple):
    c: Any
    h: Any

class LSTMStateTuple(_LSTMStateTuple):
    @property
    def dtype(self): ...

class BasicLSTMCell(LayerRNNCell):
    input_spec: Any
    def __init__(
        self,
        num_units,
        forget_bias: float = ...,
        state_is_tuple: bool = ...,
        activation: Any | None = ...,
        reuse: Any | None = ...,
        name: Any | None = ...,
        dtype: Any | None = ...,
        **kwargs
    ) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def call(self, inputs, state): ...
    def get_config(self): ...

class LSTMCell(LayerRNNCell):
    input_spec: Any
    def __init__(
        self,
        num_units,
        use_peepholes: bool = ...,
        cell_clip: Any | None = ...,
        initializer: Any | None = ...,
        num_proj: Any | None = ...,
        proj_clip: Any | None = ...,
        num_unit_shards: Any | None = ...,
        num_proj_shards: Any | None = ...,
        forget_bias: float = ...,
        state_is_tuple: bool = ...,
        activation: Any | None = ...,
        reuse: Any | None = ...,
        name: Any | None = ...,
        dtype: Any | None = ...,
        **kwargs
    ) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def call(self, inputs, state): ...
    def get_config(self): ...

class _RNNCellWrapperV1(RNNCell):
    cell: Any
    def __init__(self, cell, *args, **kwargs) -> None: ...
    def __call__(self, inputs, state, scope: Any | None = ...): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...

class DropoutWrapper(rnn_cell_wrapper_impl.DropoutWrapperBase, _RNNCellWrapperV1):
    def __init__(self, *args, **kwargs) -> None: ...

class ResidualWrapper(rnn_cell_wrapper_impl.ResidualWrapperBase, _RNNCellWrapperV1):
    def __init__(self, *args, **kwargs) -> None: ...

class DeviceWrapper(rnn_cell_wrapper_impl.DeviceWrapperBase, _RNNCellWrapperV1):
    def __init__(self, *args, **kwargs) -> None: ...

class MultiRNNCell(RNNCell):
    def __init__(self, cells, state_is_tuple: bool = ...) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size, dtype): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    def call(self, inputs, state): ...
