from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, data_flow_ops as data_flow_ops, state_ops as state_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.training import optimizer as optimizer, queue_runner as queue_runner, session_manager as session_manager, session_run_hook as session_run_hook
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

class SyncReplicasOptimizer(optimizer.Optimizer):
    def __init__(self, opt, replicas_to_aggregate, total_num_replicas: Any | None = ..., variable_averages: Any | None = ..., variables_to_average: Any | None = ..., use_locking: bool = ..., name: str = ...) -> None: ...
    def compute_gradients(self, *args, **kwargs): ...
    local_step_init_op: Any
    ready_for_local_init_op: Any
    chief_init_op: Any
    def apply_gradients(self, grads_and_vars, global_step: Any | None = ..., name: Any | None = ...): ...
    def get_chief_queue_runner(self): ...
    def get_slot(self, *args, **kwargs): ...
    def variables(self): ...
    def get_slot_names(self, *args, **kwargs): ...
    def get_init_tokens_op(self, num_tokens: int = ...): ...
    def make_session_run_hook(self, is_chief, num_tokens: int = ...): ...

class _SyncReplicasOptimizerHook(session_run_hook.SessionRunHook):
    def __init__(self, sync_optimizer, is_chief, num_tokens) -> None: ...
    def begin(self) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
