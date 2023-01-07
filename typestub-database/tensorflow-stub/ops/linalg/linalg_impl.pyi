from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_linalg_ops as gen_linalg_ops, linalg_ops as linalg_ops, map_fn as map_fn, math_ops as math_ops, special_math_ops as special_math_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

band_part: Any
cholesky: Any
cholesky_solve: Any
det: Any
slogdet: Any
diag: Any
diag_part: Any
eigh: Any
eigvalsh: Any
einsum: Any
eye: Any
inv: Any
logm: Any
lu: Any
lstsq: Any
norm: Any
qr: Any
set_diag: Any
solve: Any
sqrtm: Any
svd: Any
tensordot: Any
trace: Any
transpose: Any
triangular_solve: Any

def logdet(matrix, name: Any | None = ...): ...
def adjoint(matrix, name: Any | None = ...): ...
def matrix_exponential(input, name: Any | None = ...): ...
def banded_triangular_solve(bands, rhs, lower: bool = ..., adjoint: bool = ..., name: Any | None = ...): ...
def tridiagonal_solve(diagonals, rhs, diagonals_format: str = ..., transpose_rhs: bool = ..., conjugate_rhs: bool = ..., name: Any | None = ..., partial_pivoting: bool = ..., perturb_singular: bool = ...): ...
def tridiagonal_matmul(diagonals, rhs, diagonals_format: str = ..., name: Any | None = ...): ...
def matrix_rank(a, tol: Any | None = ..., validate_args: bool = ..., name: Any | None = ...): ...
def pinv(a, rcond: Any | None = ..., validate_args: bool = ..., name: Any | None = ...): ...
def lu_solve(lower_upper, perm, rhs, validate_args: bool = ..., name: Any | None = ...): ...
def lu_matrix_inverse(lower_upper, perm, validate_args: bool = ..., name: Any | None = ...): ...
def lu_reconstruct(lower_upper, perm, validate_args: bool = ..., name: Any | None = ...): ...
def lu_reconstruct_assertions(lower_upper, perm, validate_args): ...
def eigh_tridiagonal(alpha, beta, eigvals_only: bool = ..., select: str = ..., select_range: Any | None = ..., tol: Any | None = ..., name: Any | None = ...): ...
