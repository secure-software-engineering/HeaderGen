from typing import Any

from keras import activations as activations
from keras import backend as backend
from keras import constraints as constraints
from keras import initializers as initializers
from keras import regularizers as regularizers
from keras.src.engine import base_layer as base_layer
from keras.src.engine.input_spec import InputSpec as InputSpec
from keras.src.saving.saved_model import layer_serialization as layer_serialization
from keras.utils import control_flow_util as control_flow_util
from keras.utils import generic_utils as generic_utils
from keras.utils import tf_utils as tf_utils

RECURRENT_DROPOUT_WARNING_MSG: str

class StackedRNNCells(base_layer.Layer):
    cells: Any
    reverse_state_order: Any
    def __init__(self, cells, **kwargs) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def get_initial_state(
        self,
        inputs: Any | None = ...,
        batch_size: Any | None = ...,
        dtype: Any | None = ...,
    ): ...
    def call(
        self,
        inputs,
        states,
        constants: Any | None = ...,
        training: Any | None = ...,
        **kwargs
    ): ...
    built: bool
    def build(self, input_shape): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...

class RNN(base_layer.Layer):
    zero_output_for_mask: Any
    cell: Any
    return_sequences: Any
    return_state: Any
    go_backwards: Any
    stateful: Any
    unroll: Any
    time_major: Any
    supports_masking: bool
    input_spec: Any
    state_spec: Any
    constants_spec: Any
    def __init__(
        self,
        cell,
        return_sequences: bool = ...,
        return_state: bool = ...,
        go_backwards: bool = ...,
        stateful: bool = ...,
        unroll: bool = ...,
        time_major: bool = ...,
        **kwargs
    ) -> None: ...
    @property
    def states(self): ...
    @states.setter
    def states(self, states) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask): ...
    built: bool
    def build(self, input_shape): ...
    def get_initial_state(self, inputs): ...
    def __call__(
        self,
        inputs,
        initial_state: Any | None = ...,
        constants: Any | None = ...,
        **kwargs
    ): ...
    def call(
        self,
        inputs,
        mask: Any | None = ...,
        training: Any | None = ...,
        initial_state: Any | None = ...,
        constants: Any | None = ...,
    ): ...
    def reset_states(self, states: Any | None = ...) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Any | None = ...): ...

class AbstractRNNCell(base_layer.Layer):
    def call(self, inputs, states) -> None: ...
    @property
    def state_size(self) -> None: ...
    @property
    def output_size(self) -> None: ...
    def get_initial_state(
        self,
        inputs: Any | None = ...,
        batch_size: Any | None = ...,
        dtype: Any | None = ...,
    ): ...

class DropoutRNNCellMixin:
    def __init__(self, *args, **kwargs) -> None: ...
    def reset_dropout_mask(self) -> None: ...
    def reset_recurrent_dropout_mask(self) -> None: ...
    def get_dropout_mask_for_cell(self, inputs, training, count: int = ...): ...
    def get_recurrent_dropout_mask_for_cell(
        self, inputs, training, count: int = ...
    ): ...

class SimpleRNNCell(DropoutRNNCellMixin, base_layer.BaseRandomLayer):
    units: Any
    activation: Any
    use_bias: Any
    kernel_initializer: Any
    recurrent_initializer: Any
    bias_initializer: Any
    kernel_regularizer: Any
    recurrent_regularizer: Any
    bias_regularizer: Any
    kernel_constraint: Any
    recurrent_constraint: Any
    bias_constraint: Any
    dropout: Any
    recurrent_dropout: Any
    state_size: Any
    output_size: Any
    def __init__(
        self,
        units,
        activation: str = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        recurrent_initializer: str = ...,
        bias_initializer: str = ...,
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
    kernel: Any
    recurrent_kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs, states, training: Any | None = ...): ...
    def get_initial_state(
        self,
        inputs: Any | None = ...,
        batch_size: Any | None = ...,
        dtype: Any | None = ...,
    ): ...
    def get_config(self): ...

class SimpleRNN(RNN):
    activity_regularizer: Any
    input_spec: Any
    def __init__(
        self,
        units,
        activation: str = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        recurrent_initializer: str = ...,
        bias_initializer: str = ...,
        kernel_regularizer: Any | None = ...,
        recurrent_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        activity_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        recurrent_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        dropout: float = ...,
        recurrent_dropout: float = ...,
        return_sequences: bool = ...,
        return_state: bool = ...,
        go_backwards: bool = ...,
        stateful: bool = ...,
        unroll: bool = ...,
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
    def units(self): ...
    @property
    def activation(self): ...
    @property
    def use_bias(self): ...
    @property
    def kernel_initializer(self): ...
    @property
    def recurrent_initializer(self): ...
    @property
    def bias_initializer(self): ...
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

class GRUCell(DropoutRNNCellMixin, base_layer.BaseRandomLayer):
    units: Any
    activation: Any
    recurrent_activation: Any
    use_bias: Any
    kernel_initializer: Any
    recurrent_initializer: Any
    bias_initializer: Any
    kernel_regularizer: Any
    recurrent_regularizer: Any
    bias_regularizer: Any
    kernel_constraint: Any
    recurrent_constraint: Any
    bias_constraint: Any
    dropout: Any
    recurrent_dropout: Any
    implementation: int
    reset_after: Any
    state_size: Any
    output_size: Any
    def __init__(
        self,
        units,
        activation: str = ...,
        recurrent_activation: str = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        recurrent_initializer: str = ...,
        bias_initializer: str = ...,
        kernel_regularizer: Any | None = ...,
        recurrent_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        recurrent_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        dropout: float = ...,
        recurrent_dropout: float = ...,
        reset_after: bool = ...,
        **kwargs
    ) -> None: ...
    kernel: Any
    recurrent_kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs, states, training: Any | None = ...): ...
    def get_config(self): ...
    def get_initial_state(
        self,
        inputs: Any | None = ...,
        batch_size: Any | None = ...,
        dtype: Any | None = ...,
    ): ...

class GRU(RNN):
    activity_regularizer: Any
    input_spec: Any
    def __init__(
        self,
        units,
        activation: str = ...,
        recurrent_activation: str = ...,
        use_bias: bool = ...,
        kernel_initializer: str = ...,
        recurrent_initializer: str = ...,
        bias_initializer: str = ...,
        kernel_regularizer: Any | None = ...,
        recurrent_regularizer: Any | None = ...,
        bias_regularizer: Any | None = ...,
        activity_regularizer: Any | None = ...,
        kernel_constraint: Any | None = ...,
        recurrent_constraint: Any | None = ...,
        bias_constraint: Any | None = ...,
        dropout: float = ...,
        recurrent_dropout: float = ...,
        return_sequences: bool = ...,
        return_state: bool = ...,
        go_backwards: bool = ...,
        stateful: bool = ...,
        unroll: bool = ...,
        reset_after: bool = ...,
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
    def units(self): ...
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
    @property
    def implementation(self): ...
    @property
    def reset_after(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

class LSTMCell(DropoutRNNCellMixin, base_layer.BaseRandomLayer):
    units: Any
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
    implementation: int
    state_size: Any
    output_size: Any
    def __init__(
        self,
        units,
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
    kernel: Any
    recurrent_kernel: Any
    bias: Any
    built: bool
    def build(self, input_shape): ...
    def call(self, inputs, states, training: Any | None = ...): ...
    def get_config(self): ...
    def get_initial_state(
        self,
        inputs: Any | None = ...,
        batch_size: Any | None = ...,
        dtype: Any | None = ...,
    ): ...

class PeepholeLSTMCell(LSTMCell):
    def __init__(
        self,
        units,
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
    input_gate_peephole_weights: Any
    forget_gate_peephole_weights: Any
    output_gate_peephole_weights: Any
    def build(self, input_shape) -> None: ...

class LSTM(RNN):
    activity_regularizer: Any
    input_spec: Any
    def __init__(
        self,
        units,
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
        dropout: float = ...,
        recurrent_dropout: float = ...,
        return_sequences: bool = ...,
        return_state: bool = ...,
        go_backwards: bool = ...,
        stateful: bool = ...,
        unroll: bool = ...,
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
    def units(self): ...
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
    @property
    def implementation(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
