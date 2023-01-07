import abc
from tensorflow.core.protobuf.tpu import optimization_parameters_pb2 as optimization_parameters_pb2, tpu_embedding_configuration_pb2 as tpu_embedding_configuration_pb2
from tensorflow.python.distribute import sharded_variable as sharded_variable
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import init_ops_v2 as init_ops_v2, variables as tf_variables
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.types import core as core
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Callable, Optional, Text, Tuple, TypeVar, Union

TableVariable = TypeVar('TableVariable', sharded_variable.ShardedVariable, tf_variables.Variable)
SlotVarCreationFnType: Any
ClipValueType = Union[Tuple[float, float], float]

class _Optimizer(metaclass=abc.ABCMeta):
    learning_rate: Any
    use_gradient_accumulation: Any
    clip_weight_min: Any
    clip_weight_max: Any
    weight_decay_factor: Any
    multiply_weight_decay_factor_by_learning_rate: Any
    slot_variable_creation_fn: Any
    def __init__(self, learning_rate: Union[float, Callable[[], float]], use_gradient_accumulation: bool, clip_weight_min: Optional[float], clip_weight_max: Optional[float], weight_decay_factor: Optional[float], multiply_weight_decay_factor_by_learning_rate: bool, clipvalue: Optional[ClipValueType] = ..., slot_variable_creation_fn: Optional[SlotVarCreationFnType] = ...) -> None: ...

class SGD(_Optimizer):
    def __init__(self, learning_rate: Union[float, Callable[[], float]] = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: bool = ..., clipvalue: Optional[ClipValueType] = ...) -> None: ...

class Adagrad(_Optimizer):
    initial_accumulator_value: Any
    def __init__(self, learning_rate: Union[float, Callable[[], float]] = ..., initial_accumulator_value: float = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: bool = ..., slot_variable_creation_fn: Optional[SlotVarCreationFnType] = ..., clipvalue: Optional[ClipValueType] = ...) -> None: ...

class FTRL(_Optimizer):
    initial_accumulator_value: Any
    learning_rate_power: Any
    l1_regularization_strength: Any
    l2_regularization_strength: Any
    beta: Any
    multiply_linear_by_learning_rate: Any
    allow_zero_accumulator: Any
    def __init__(self, learning_rate: Union[float, Callable[[], float]] = ..., learning_rate_power: float = ..., l1_regularization_strength: float = ..., l2_regularization_strength: float = ..., beta: float = ..., initial_accumulator_value: float = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: bool = ..., slot_variable_creation_fn: Optional[SlotVarCreationFnType] = ..., clipvalue: Optional[ClipValueType] = ..., multiply_linear_by_learning_rate: bool = ..., allow_zero_accumulator: bool = ...) -> None: ...

class Adam(_Optimizer):
    beta_1: Any
    beta_2: Any
    epsilon: Any
    lazy_adam: Any
    sum_inside_sqrt: Any
    def __init__(self, learning_rate: Union[float, Callable[[], float]] = ..., beta_1: float = ..., beta_2: float = ..., epsilon: float = ..., lazy_adam: bool = ..., sum_inside_sqrt: bool = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: bool = ..., slot_variable_creation_fn: Optional[SlotVarCreationFnType] = ..., clipvalue: Optional[ClipValueType] = ...) -> None: ...

class TableConfig:
    vocabulary_size: Any
    dim: Any
    initializer: Any
    optimizer: Any
    combiner: Any
    name: Any
    def __init__(self, vocabulary_size: int, dim: int, initializer: Optional[Callable[[Any], None]], optimizer: Optional[_Optimizer] = ..., combiner: Text = ..., name: Optional[Text] = ...) -> None: ...

class FeatureConfig:
    table: Any
    max_sequence_length: Any
    name: Any
    validate_weights_and_indices: Any
    def __init__(self, table: TableConfig, max_sequence_length: int = ..., validate_weights_and_indices: bool = ..., name: Optional[Text] = ...) -> None: ...

def log_tpu_embedding_configuration(config: tpu_embedding_configuration_pb2.TPUEmbeddingConfiguration) -> None: ...
