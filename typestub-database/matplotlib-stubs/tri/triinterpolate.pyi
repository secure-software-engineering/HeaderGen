from typing import Any

class TriInterpolator:
    def __init__(self, triangulation, z, trifinder: Any | None = ...) -> None: ...
    _docstring__call__: str

class LinearTriInterpolator(TriInterpolator):
    def __init__(self, triangulation, z, trifinder: Any | None = ...) -> None: ...
    def __call__(self, x, y): ...
    def gradient(self, x, y): ...

class CubicTriInterpolator(TriInterpolator):
    def __init__(self, triangulation, z, kind: str = ..., trifinder: Any | None = ..., dz: Any | None = ...) -> None: ...
    def __call__(self, x, y): ...
    def gradient(self, x, y): ...

class _ReducedHCT_Element:
    M: Any
    M0: Any
    M1: Any
    M2: Any
    rotate_dV: Any
    rotate_d2V: Any
    n_gauss: int
    gauss_pts: Any
    gauss_w: Any
    E: Any
    J0_to_J1: Any
    J0_to_J2: Any
    def get_function_values(self, alpha, ecc, dofs): ...
    def get_function_derivatives(self, alpha, J, ecc, dofs): ...
    def get_function_hessians(self, alpha, J, ecc, dofs): ...
    def get_d2Sidksij2(self, alpha, ecc): ...
    def get_bending_matrices(self, J, ecc): ...
    def get_Hrot_from_J(self, J, return_area: bool = ...): ...
    def get_Kff_and_Ff(self, J, ecc, triangles, Uc): ...

class _DOF_estimator:
    z: Any
    dz: Any
    def __init__(self, interpolator, **kwargs) -> None: ...
    def compute_dz(self, **kwargs) -> None: ...
    def compute_dof_from_df(self): ...
    @staticmethod
    def get_dof_vec(tri_z, tri_dz, J): ...

class _DOF_estimator_user(_DOF_estimator):
    def compute_dz(self, dz): ...

class _DOF_estimator_geom(_DOF_estimator):
    def compute_dz(self): ...
    def compute_geom_weights(self): ...
    def compute_geom_grads(self): ...

class _DOF_estimator_min_E(_DOF_estimator_geom):
    def __init__(self, Interpolator) -> None: ...
    def compute_dz(self): ...

class _Sparse_Matrix_coo:
    vals: Any
    rows: Any
    cols: Any
    def __init__(self, vals, rows, cols, shape) -> None: ...
    def dot(self, V): ...
    def compress_csc(self) -> None: ...
    def compress_csr(self) -> None: ...
    def to_dense(self): ...
    @property
    def diag(self): ...
