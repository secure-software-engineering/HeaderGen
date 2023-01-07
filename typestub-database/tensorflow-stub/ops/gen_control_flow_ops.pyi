from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def abort(error_msg: str = ..., exit_without_error: bool = ..., name: Any | None = ...): ...

Abort: Any

def abort_eager_fallback(error_msg, exit_without_error, name, ctx): ...
def control_trigger(name: Any | None = ...): ...

ControlTrigger: Any

def control_trigger_eager_fallback(name, ctx): ...
def enter(data, frame_name, is_constant: bool = ..., parallel_iterations: int = ..., name: Any | None = ...): ...

Enter: Any

def enter_eager_fallback(data, frame_name, is_constant, parallel_iterations, name, ctx): ...

Exit: Any

def loop_cond(input, name: Any | None = ...): ...

LoopCond: Any

def loop_cond_eager_fallback(input, name, ctx): ...

class _MergeOutput(NamedTuple):
    output: Any
    value_index: Any

def merge(inputs, name: Any | None = ...): ...

Merge: Any

def merge_eager_fallback(inputs, name, ctx): ...
def next_iteration(data, name: Any | None = ...): ...

NextIteration: Any

def next_iteration_eager_fallback(data, name, ctx): ...
def no_op(name: Any | None = ...): ...

NoOp: Any

def no_op_eager_fallback(name, ctx): ...
def ref_enter(data, frame_name, is_constant: bool = ..., parallel_iterations: int = ..., name: Any | None = ...): ...

RefEnter: Any

def ref_enter_eager_fallback(data, frame_name, is_constant, parallel_iterations, name, ctx) -> None: ...
def ref_exit(data, name: Any | None = ...): ...

RefExit: Any

def ref_exit_eager_fallback(data, name, ctx) -> None: ...

class _RefMergeOutput(NamedTuple):
    output: Any
    value_index: Any

def ref_merge(inputs, name: Any | None = ...): ...

RefMerge: Any

def ref_merge_eager_fallback(inputs, name, ctx) -> None: ...
def ref_next_iteration(data, name: Any | None = ...): ...

RefNextIteration: Any

def ref_next_iteration_eager_fallback(data, name, ctx) -> None: ...
def ref_select(index, inputs, name: Any | None = ...): ...

RefSelect: Any

def ref_select_eager_fallback(index, inputs, name, ctx) -> None: ...

class _RefSwitchOutput(NamedTuple):
    output_false: Any
    output_true: Any

def ref_switch(data, pred, name: Any | None = ...): ...

RefSwitch: Any

def ref_switch_eager_fallback(data, pred, name, ctx) -> None: ...

class _SwitchOutput(NamedTuple):
    output_false: Any
    output_true: Any

def switch(data, pred, name: Any | None = ...): ...

Switch: Any

def switch_eager_fallback(data, pred, name, ctx): ...
