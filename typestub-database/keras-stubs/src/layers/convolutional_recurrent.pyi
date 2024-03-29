from typing import Any

from keras import activations as activations
from keras import backend as backend
from keras import constraints as constraints
from keras import initializers as initializers
from keras import regularizers as regularizers
from keras.src.engine import base_layer as base_layer
from keras.src.engine.input_spec import InputSpec as InputSpec
from keras.src.layers.recurrent import RNN as RNN
from keras.src.layers.recurrent import DropoutRNNCellMixin as DropoutRNNCellMixin
from keras.utils import conv_utils as conv_utils
from keras.utils import generic_utils as generic_utils
from keras.utils import tf_utils as tf_utils

class ConvRNN(RNN):
    rank: Any
    input_spec: Any
    states: Any
    def __init__(
        self,
        rank,
        cell,
        return_sequences: bool = ...,
        return_state: bool = ...,
        go_backwards: bool = ...,
        stateful: bool = ...,
        unroll: bool = ...,
        **kwargs
    ) -> None: ...
    def compute_output_shape(self, input_shape): ...
    state_spec: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def get_initial_state(self, inputs): ...
    def call(
        self,
        inputs,
        mask: Any | None = ...,
        training: Any | None = ...,
        initial_state: Any | None = ...,
        constants: Any | None = ...,
    ): ...
    def reset_states(self, states: Any | None = ...): ...

class ConvLSTMCell(DropoutRNNCellMixin, base_layer.BaseRandomLayer):
    rank: Any
    filters: Any
    kernel_size: Any
    strides: Any
    padding: Any
    data_format: Any
    dilation_rate: Any
    activation: Any
    recurrent_activation: Any
    use_bias: Any
    kernel_initializer: Any
    recurrent_initializer: Any
    bias_initializer: Any
    unit_forget_bias: Any
    kernel_regularizer: Any
    recurrent_regularizer: Any
    bias_regularizer: Any
    kernel_constraint: Any
    recurrent_constraint: Any
    bias_constraint: Any
    dropout: Any
    recurrent_dropout: Any
    state_size: Any
    def __init__(
        self,
        rank,
        filters,
        kernel_size,
        strides: int = ...,
        padding: str = ...,
        data_format: Any | None = ...,
        dilation_rate: int = ...,
        activation: str = ...,
        recurrent_activation: str = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        recurrent_initializer: str = ...,
        bias_initializer: str = ...,
        unit_forget_bias: bool = ...,
        kernel_regularizer: Any | None = ...,
        recurrent_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        recurrent_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        dropout: float = ...,
        recurrent_dropout: float = ...,
        **kwargs
    ) -> None: ...
    kernel_shape: Any
    kernel: Any
    recurrent_kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape): ...
    def call(self, inputs, states, training: Any | None = ...): ...
    def input_conv(self, x, w, b: Any | None = ..., padding: str = ...): ...
    def recurrent_conv(self, x, w): ...
    def get_config(self): ...

class ConvLSTM(ConvRNN):
    activity_regularizer: Any
    def __init__(
        self,
        rank,
        filters,
        kernel_size,
        strides: int = ...,
        padding: str = ...,
        data_format: Any | None = ...,
        dilation_rate: int = ...,
        activation: str = ...,
        recurrent_activation: str = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        recurrent_initializer: str = ...,
        bias_initializer: str = ...,
        unit_forget_bias: bool = ...,
        kernel_regularizer: Any | None = ...,
        recurrent_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        activity_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        recurrent_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        return_sequences: bool = ...,
        return_state: bool = ...,
        go_backwards: bool = ...,
        stateful: bool = ...,
        dropout: float = ...,
        recurrent_dropout: float = ...,
        **kwargs
    ) -> None: ...
    def call(
        self,
        inputs,
        mask: Any | None = ...,
        training: Any | None = ...,
        initial_state: Any | None = ...,
    ): ...
    @property
    def filters(self): ...
    @property
    def kernel_size(self): ...
    @property
    def strides(self): ...
    @property
    def padding(self): ...
    @property
    def data_format(self): ...
    @property
    def dilation_rate(self): ...
    @property
    def activation(self): ...
    @property
    def recurrent_activation(self): ...
    @property
    def use_bias(self): ...
    @property
    def kernel_initializer(self): ...
    @property
    def recurrent_initializer(self): ...
    @property
    def bias_initializer(self): ...
    @property
    def unit_forget_bias(self): ...
    @property
    def kernel_regularizer(self): ...
    @property
    def recurrent_regularizer(self): ...
    @property
    def bias_regularizer(self): ...
    @property
    def kernel_constraint(self): ...
    @property
    def recurrent_constraint(self): ...
    @property
    def bias_constraint(self): ...
    @property
    def dropout(self): ...
    @property
    def recurrent_dropout(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

class ConvLSTM1D(ConvLSTM):
    def __init__(
        self,
        filters,
        kernel_size,
        strides: int = ...,
        padding: str = ...,
        data_format: Any | None = ...,
        dilation_rate: int = ...,
        activation: str = ...,
        recurrent_activation: str = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        recurrent_initializer: str = ...,
        bias_initializer: str = ...,
        unit_forget_bias: bool = ...,
        kernel_regularizer: Any | None = ...,
        recurrent_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        activity_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        recurrent_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        return_sequences: bool = ...,
        return_state: bool = ...,
        go_backwards: bool = ...,
        stateful: bool = ...,
        dropout: float = ...,
        recurrent_dropout: float = ...,
        **kwargs
    ) -> None: ...

class ConvLSTM2D(ConvLSTM):
    def __init__(
        self,
        filters,
        kernel_size,
        strides=...,
        padding: str = ...,
        data_format: Any | None = ...,
        dilation_rate=...,
        activation: str = ...,
        recurrent_activation: str = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        recurrent_initializer: str = ...,
        bias_initializer: str = ...,
        unit_forget_bias: bool = ...,
        kernel_regularizer: Any | None = ...,
        recurrent_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        activity_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        recurrent_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        return_sequences: bool = ...,
        return_state: bool = ...,
        go_backwards: bool = ...,
        stateful: bool = ...,
        dropout: float = ...,
        recurrent_dropout: float = ...,
        **kwargs
    ) -> None: ...

class ConvLSTM3D(ConvLSTM):
    def __init__(
        self,
        filters,
        kernel_size,
        strides=...,
        padding: str = ...,
        data_format: Any | None = ...,
        dilation_rate=...,
        activation: str = ...,
        recurrent_activation: str = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        recurrent_initializer: str = ...,
        bias_initializer: str = ...,
        unit_forget_bias: bool = ...,
        kernel_regularizer: Any | None = ...,
        recurrent_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        activity_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        recurrent_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        return_sequences: bool = ...,
        return_state: bool = ...,
        go_backwards: bool = ...,
        stateful: bool = ...,
        dropout: float = ...,
        recurrent_dropout: float = ...,
        **kwargs
    ) -> None: ...
