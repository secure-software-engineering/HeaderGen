import abc
from statsmodels.compat.python import with_metaclass as with_metaclass
from statsmodels.tools.linalg import transf_constraints as transf_constraints
from typing import Any

def compute_all_knots(x, df, degree): ...
def make_bsplines_basis(x, df, degree): ...
def get_knots_bsplines(x: Any | None = ..., df: Any | None = ..., knots: Any | None = ..., degree: int = ..., spacing: str = ..., lower_bound: Any | None = ..., upper_bound: Any | None = ..., all_knots: Any | None = ...): ...
def get_covder2(smoother, k_points: int = ..., integration_points: Any | None = ..., skip_ctransf: bool = ..., deriv: int = ...): ...
def make_poly_basis(x, degree, intercept: bool = ...): ...

class UnivariateGamSmoother(metaclass=abc.ABCMeta):
    x: Any
    constraints: Any
    variable_name: Any
    ctransf: Any
    basis: Any
    der_basis: Any
    der2_basis: Any
    cov_der2: Any
    dim_basis: Any
    col_names: Any
    def __init__(self, x, constraints: Any | None = ..., variable_name: str = ...) -> None: ...

class UnivariateGenericSmoother(UnivariateGamSmoother):
    basis: Any
    der_basis: Any
    der2_basis: Any
    cov_der2: Any
    def __init__(self, x, basis, der_basis, der2_basis, cov_der2, variable_name: str = ...) -> None: ...

class UnivariatePolynomialSmoother(UnivariateGamSmoother):
    degree: Any
    def __init__(self, x, degree, variable_name: str = ...) -> None: ...

class UnivariateBSplines(UnivariateGamSmoother):
    degree: Any
    df: Any
    include_intercept: Any
    knots: Any
    covder2_kwds: Any
    def __init__(self, x, df, degree: int = ..., include_intercept: bool = ..., constraints: Any | None = ..., variable_name: str = ..., covder2_kwds: Any | None = ..., **knot_kwds) -> None: ...
    def transform(self, x_new, deriv: int = ..., skip_ctransf: bool = ...): ...

class UnivariateCubicSplines(UnivariateGamSmoother):
    degree: int
    df: Any
    transform_data_method: Any
    x: Any
    knots: Any
    def __init__(self, x, df, constraints: Any | None = ..., transform: str = ..., variable_name: str = ...) -> None: ...
    domain_low: Any
    domain_upp: Any
    domain_diff: Any
    def transform_data(self, x, initialize: bool = ...): ...
    def transform(self, x_new): ...

class UnivariateCubicCyclicSplines(UnivariateGamSmoother):
    degree: int
    df: Any
    x: Any
    knots: Any
    def __init__(self, x, df, constraints: Any | None = ..., variable_name: str = ...) -> None: ...
    def transform(self, x_new): ...

class AdditiveGamSmoother(metaclass=abc.ABCMeta):
    x: Any
    include_intercept: Any
    variable_names: Any
    smoothers: Any
    basis: Any
    dim_basis: Any
    penalty_matrices: Any
    col_names: Any
    mask: Any
    def __init__(self, x, variable_names: Any | None = ..., include_intercept: bool = ..., **kwargs) -> None: ...
    def transform(self, x_new): ...

class GenericSmoothers(AdditiveGamSmoother):
    smoothers: Any
    def __init__(self, x, smoothers) -> None: ...

class PolynomialSmoother(AdditiveGamSmoother):
    degrees: Any
    def __init__(self, x, degrees, variable_names: Any | None = ...) -> None: ...

class BSplines(AdditiveGamSmoother):
    degrees: Any
    dfs: Any
    knot_kwds: Any
    constraints: Any
    def __init__(self, x, df, degree, include_intercept: bool = ..., constraints: Any | None = ..., variable_names: Any | None = ..., knot_kwds: Any | None = ...) -> None: ...

class CubicSplines(AdditiveGamSmoother):
    dfs: Any
    constraints: Any
    transform: Any
    def __init__(self, x, df, constraints: str = ..., transform: str = ..., variable_names: Any | None = ...) -> None: ...

class CyclicCubicSplines(AdditiveGamSmoother):
    dfs: Any
    constraints: Any
    def __init__(self, x, df, constraints: Any | None = ..., variable_names: Any | None = ...) -> None: ...
