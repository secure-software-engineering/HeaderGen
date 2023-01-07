import enum
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import op_def_registry as op_def_registry, ops as ops, registry as registry, sparse_tensor as sparse_tensor
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, tensor_array_ops as tensor_array_ops
from tensorflow.python.util import nest as nest, object_identity as object_identity, tf_decorator as tf_decorator
from typing import Any

ASYNC_STATEFUL_OPS: Any
LEGACY_RANDOM_OPS: Any

def op_is_stateful(op): ...

class ResourceType(enum.Enum):
    READ_ONLY: str
    READ_WRITE: str

def collective_manager_ids_from_op(op): ...

class AutomaticControlDependencies:
    ops_which_must_run: Any
    record_initial_resource_uses: Any
    record_uses_of_resource_ids: Any
    def __init__(self, record_initial_resource_uses: bool = ..., record_uses_of_resource_ids: Any | None = ...) -> None: ...
    def mark_as_return(self, tensor): ...
    def __enter__(self): ...
    collective_manager_ids_used: Any
    def __exit__(self, unused_type, unused_value, unused_traceback) -> None: ...

def register_acd_resource_resolver(f): ...
def automatic_control_dependencies(f): ...
