from tensorflow.core.protobuf.tpu import optimization_parameters_pb2 as optimization_parameters_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, partitioned_variables as partitioned_variables, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple, Optional

TRAINING: Any
INFERENCE: Any

class TableConfig:
    def __new__(cls, vocabulary_size, dimension, initializer: Any | None = ..., combiner: str = ..., hot_id_replication: bool = ..., learning_rate: Any | None = ..., learning_rate_fn: Any | None = ..., optimization_parameters: Any | None = ...): ...

class FeatureConfig:
    def __new__(cls, table_id, max_sequence_length: int = ..., weight_key: Any | None = ...): ...

class EnqueueData:
    def __new__(cls, embedding_indices, sample_indices: Any | None = ..., aggregation_weights: Any | None = ...): ...
    @staticmethod
    def from_sparse_tensor(sp_tensor, weights: Any | None = ...): ...

class RaggedEnqueueData:
    def __new__(cls, embedding_indices, sample_splits: Any | None = ..., aggregation_weights: Any | None = ...): ...
    @staticmethod
    def from_ragged_tensor(rg_tensor, weights: Any | None = ...): ...

def get_enqueue_datas_list_from_sparse_tensors_list(sp_tensors_list): ...
def get_enqueue_datas_list_from_ragged_tensors_list(rg_tensors_list): ...

class AdamSlotVariableNames(NamedTuple):
    m: Any
    v: Any

class AdagradSlotVariableNames(NamedTuple):
    accumulator: Any

class MomentumSlotVariableNames(NamedTuple):
    momenta: Any

class AdagradMomentumSlotVariableNames(NamedTuple):
    accumulator: Any
    momenta: Any

class RMSPropSlotVariableNames(NamedTuple):
    ms: Any
    mom: Any

class ProximalAdagradSlotVariableNames(NamedTuple):
    accumulator: Any

class FtrlSlotVariableNames(NamedTuple):
    accumulator: Any
    linear: Any

class ProximalYogiSlotVariableNames(NamedTuple):
    v: Any
    m: Any

class FrequencyEstimatorSlotVariableNames(NamedTuple):
    last_hit_step: Any

class AdamSlotVariables(NamedTuple):
    m: Any
    v: Any

class MomentumSlotVariables(NamedTuple):
    momenta: Any

class AdagradMomentumSlotVariables(NamedTuple):
    accumulator: Any
    momenta: Any

class RMSPropSlotVariables(NamedTuple):
    ms: Any
    mom: Any

class AdagradSlotVariables(NamedTuple):
    accumulator: Any

class ProximalAdagradSlotVariables(NamedTuple):
    accumulator: Any

class FtrlSlotVariable(NamedTuple):
    accumulator: Any
    linear: Any

class ProximalYogiSlotVariables(NamedTuple):
    v: Any
    m: Any

class FrequencyEstimatorSlotVariables(NamedTuple):
    last_hit_step: Any

class VariablesAndOps(NamedTuple):
    embedding_variables_by_table: Any
    slot_variables_by_table: Any
    load_ops: Any
    retrieve_ops: Any

class _OptimizationParameters:
    learning_rate: Any
    use_gradient_accumulation: Any
    clip_weight_min: Any
    clip_weight_max: Any
    weight_decay_factor: Any
    multiply_weight_decay_factor_by_learning_rate: Any
    clip_gradient_min: Any
    clip_gradient_max: Any
    def __init__(self, learning_rate: float, use_gradient_accumulation: bool, clip_weight_min: Optional[float], clip_weight_max: Optional[float], weight_decay_factor: Optional[float], multiply_weight_decay_factor_by_learning_rate: Optional[bool], clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class AdagradParameters(_OptimizationParameters):
    initial_accumulator: Any
    def __init__(self, learning_rate: float, initial_accumulator: float = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[bool] = ..., clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class AdagradMomentumParameters(_OptimizationParameters):
    momentum: Any
    use_nesterov: Any
    exponent: Any
    beta2: Any
    initial_accumulator: Any
    def __init__(self, learning_rate: float, momentum: float, use_nesterov: bool = ..., exponent: float = ..., beta2: float = ..., initial_accumulator: float = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[bool] = ..., clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class ProximalAdagradParameters(_OptimizationParameters):
    initial_accumulator: Any
    l1_regularization_strength: Any
    l2_regularization_strength: Any
    def __init__(self, learning_rate: float, initial_accumulator: float = ..., l1_regularization_strength: float = ..., l2_regularization_strength: float = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[bool] = ..., clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class AdamParameters(_OptimizationParameters):
    beta1: Any
    beta2: Any
    epsilon: Any
    lazy_adam: Any
    sum_inside_sqrt: Any
    def __init__(self, learning_rate: float, beta1: float = ..., beta2: float = ..., epsilon: float = ..., lazy_adam: bool = ..., sum_inside_sqrt: bool = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[bool] = ..., clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class FtrlParameters(_OptimizationParameters):
    learning_rate_power: Any
    initial_accumulator_value: Any
    initial_linear_value: float
    l1_regularization_strength: Any
    l2_regularization_strength: Any
    multiply_linear_by_learning_rate: Any
    beta: Any
    allow_zero_accumulator: Any
    def __init__(self, learning_rate: float, learning_rate_power: float = ..., initial_accumulator_value: float = ..., l1_regularization_strength: float = ..., l2_regularization_strength: float = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[bool] = ..., multiply_linear_by_learning_rate: bool = ..., beta: float = ..., allow_zero_accumulator: bool = ..., clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class ProximalYogiParameters(_OptimizationParameters):
    beta1: Any
    beta2: Any
    epsilon: Any
    l1_regularization_strength: Any
    l2_regularization_strength: Any
    initial_accumulator_value: Any
    def __init__(self, learning_rate: float = ..., beta1: float = ..., beta2: float = ..., epsilon: float = ..., l1_regularization_strength: float = ..., l2_regularization_strength: float = ..., initial_accumulator_value: float = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[bool] = ..., clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class MomentumParameters(_OptimizationParameters):
    momentum: Any
    use_nesterov: Any
    def __init__(self, learning_rate: float, momentum: float, use_nesterov: bool = ..., use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[bool] = ..., clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class RMSPropParameters(_OptimizationParameters):
    rho: Any
    momentum: Any
    epsilon: Any
    def __init__(self, learning_rate: float, rho: float, momentum: float, epsilon: float, use_gradient_accumulation: bool = ..., clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[bool] = ..., clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class StochasticGradientDescentParameters(_OptimizationParameters):
    def __init__(self, learning_rate: float, clip_weight_min: Optional[float] = ..., clip_weight_max: Optional[float] = ..., weight_decay_factor: Optional[float] = ..., multiply_weight_decay_factor_by_learning_rate: Optional[bool] = ..., clip_gradient_min: Optional[float] = ..., clip_gradient_max: Optional[float] = ...) -> None: ...

class FrequencyEstimatorParameters(_OptimizationParameters):
    tau: Any
    max_delta: Any
    outlier_threshold: Any
    weight_exponent: Any
    def __init__(self, tau: float, max_delta: float, outlier_threshold: float, weight_exponent: float) -> None: ...

class DeviceConfig(NamedTuple):
    num_hosts: Any
    num_cores: Any
    job_name: Any

class TPUEmbedding:
    def __init__(self, table_to_config_dict, feature_to_config_dict, batch_size, mode, master: Any | None = ..., optimization_parameters: Any | None = ..., cluster_def: Any | None = ..., pipeline_execution_with_tensor_core: bool = ..., partition_strategy: str = ..., profile_data_directory: Any | None = ..., device_config: Any | None = ..., master_job_name: Any | None = ...) -> None: ...
    @property
    def hosts(self): ...
    @property
    def num_cores_per_host(self): ...
    @property
    def num_cores(self): ...
    @property
    def batch_size_per_core(self): ...
    @property
    def config_proto(self): ...
    @property
    def table_to_config_dict(self): ...
    @property
    def feature_to_config_dict(self): ...
    @property
    def table_to_features_dict(self): ...
    @property
    def optimization_parameters(self): ...
    def create_variables_and_ops(self, embedding_variable_name_by_table: Any | None = ..., slot_variable_names_by_table: Any | None = ...): ...
    def generate_enqueue_ops(self, enqueue_datas_list, mode_override: Any | None = ..., ragged: bool = ...): ...
    def get_activations(self): ...
    def generate_send_gradients_op(self, feature_to_gradient_dict, step: Any | None = ...): ...

class _OptimizerHandler:
    def __init__(self, optimization_parameters) -> None: ...
    def get_optimization_parameters(self): ...
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table) -> None: ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto) -> None: ...

class _AdagradHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _AdagradMomentumHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _ProximalAdagradHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _AdamHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _FtrlHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _ProximalYogiHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _MomentumHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _RMSPropHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _FrequencyEstimatorHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table): ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...

class _StochasticGradientDescentHandler(_OptimizerHandler):
    def set_optimization_parameters(self, table_descriptor) -> None: ...
    def get_default_slot_variable_names(self, table) -> None: ...
    def create_variables_and_ops(self, table, slot_variable_names, num_hosts, table_config, table_variables, config_proto): ...
