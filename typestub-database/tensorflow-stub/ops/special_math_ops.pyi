from tensorflow.compiler.tf2xla.ops import gen_xla_ops as gen_xla_ops
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_linalg_ops as gen_linalg_ops, gen_special_math_ops as gen_special_math_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def lbeta(x, name: Any | None = ...): ...
def dawsn(x, name: Any | None = ...): ...
def expint(x, name: Any | None = ...): ...
def fresnel_cos(x, name: Any | None = ...): ...
def fresnel_sin(x, name: Any | None = ...): ...
def spence(x, name: Any | None = ...): ...
def bessel_i0(x, name: Any | None = ...): ...
def bessel_i0e(x, name: Any | None = ...): ...
def bessel_i1(x, name: Any | None = ...): ...
def bessel_i1e(x, name: Any | None = ...): ...
def bessel_k0(x, name: Any | None = ...): ...
def bessel_k0e(x, name: Any | None = ...): ...
def bessel_k1(x, name: Any | None = ...): ...
def bessel_k1e(x, name: Any | None = ...): ...
def bessel_j0(x, name: Any | None = ...): ...
def bessel_j1(x, name: Any | None = ...): ...
def bessel_y0(x, name: Any | None = ...): ...
def bessel_y1(x, name: Any | None = ...): ...
def einsum(equation, *inputs, **kwargs): ...
