from tensorflow.core.framework import tensor_pb2 as tensor_pb2
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import core as core
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.util import compat as compat
from typing import Any

def quick_execute(op_name, num_outputs, inputs, attrs, ctx, name: Any | None = ...): ...
def execute_with_cancellation(op_name, num_outputs, inputs, attrs, ctx, cancellation_manager, name: Any | None = ...): ...
def execute_with_callbacks(op_name, num_outputs, inputs, attrs, ctx, name: Any | None = ...): ...
execute = quick_execute

def must_record_gradient(): ...
def record_gradient(unused_op_name, unused_inputs, unused_attrs, unused_outputs) -> None: ...
def make_float(v, arg_name): ...
def make_int(v, arg_name): ...
def make_str(v, arg_name): ...
def make_bool(v, arg_name): ...
def make_type(v, arg_name): ...
def make_shape(v, arg_name): ...
def make_tensor(v, arg_name): ...
def args_to_matching_eager(l, ctx, allowed_dtypes, default_dtype: Any | None = ...): ...
def convert_to_mixed_eager_tensors(values, ctx): ...
def args_to_mixed_eager_tensors(lists, ctx): ...
