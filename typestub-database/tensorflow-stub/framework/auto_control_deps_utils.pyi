from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.util import object_identity as object_identity
from typing import Any

READ_ONLY_RESOURCE_INPUTS_ATTR: str
RESOURCE_READ_OPS: Any
COLLECTIVE_MANAGER_IDS: str

def register_read_only_resource_op(op_type) -> None: ...
def get_read_only_resource_input_indices_graph(func_graph): ...
def get_read_write_resource_inputs(op): ...
