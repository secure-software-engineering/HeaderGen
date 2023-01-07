from tensorflow.python.autograph.operators import py_builtins as py_builtins, variables as variables
from tensorflow.python.autograph.utils import ag_logging as ag_logging, misc as misc, tensors as tensors
from tensorflow.python.data.experimental.ops import take_while_ops as take_while_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors_impl as errors_impl, func_graph as func_graph, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util as control_flow_util, math_ops as math_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.types import distribute as distribute
from tensorflow.python.util import nest as nest
from typing import Any

PYTHON_MAX_ITERATIONS: int
WARN_INEFFICIENT_UNROLL: bool
INEFFICIENT_UNROLL_MIN_ITERATIONS: int
INEFFICIENT_UNROLL_MIN_OPS: int

def verify_single_cond_var(name, body_var, orelse_var) -> None: ...
def for_stmt(iter_, extra_test, body, get_state, set_state, symbol_names, opts) -> None: ...
def while_stmt(test, body, get_state, set_state, symbol_names, opts) -> None: ...

class _PythonLoopChecker:
    iterations: int
    check_inefficient_unroll: Any
    check_op_count_after_iteration: bool
    def __init__(self) -> None: ...
    ops_before_iteration: Any
    def before_iteration(self) -> None: ...
    def after_iteration(self) -> None: ...

LEGAL_LOOP_TYPES: str

def if_stmt(cond, body, orelse, get_state, set_state, symbol_names, nouts) -> None: ...
