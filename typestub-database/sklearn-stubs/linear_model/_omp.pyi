from ..base import MultiOutputMixin as MultiOutputMixin, RegressorMixin as RegressorMixin
from ..model_selection import check_cv as check_cv
from ..utils import as_float_array as as_float_array, check_array as check_array
from ..utils.fixes import delayed as delayed
from ._base import LinearModel as LinearModel
from typing import Any

premature: str

def orthogonal_mp(X, y, *, n_nonzero_coefs: Any | None = ..., tol: Any | None = ..., precompute: bool = ..., copy_X: bool = ..., return_path: bool = ..., return_n_iter: bool = ...): ...
def orthogonal_mp_gram(Gram, Xy, *, n_nonzero_coefs: Any | None = ..., tol: Any | None = ..., norms_squared: Any | None = ..., copy_Gram: bool = ..., copy_Xy: bool = ..., return_path: bool = ..., return_n_iter: bool = ...): ...

class OrthogonalMatchingPursuit(MultiOutputMixin, RegressorMixin, LinearModel):
    n_nonzero_coefs: Any
    tol: Any
    fit_intercept: Any
    normalize: Any
    precompute: Any
    def __init__(self, *, n_nonzero_coefs: Any | None = ..., tol: Any | None = ..., fit_intercept: bool = ..., normalize: str = ..., precompute: str = ...) -> None: ...
    n_nonzero_coefs_: Any
    coef_: Any
    def fit(self, X, y): ...

class OrthogonalMatchingPursuitCV(RegressorMixin, LinearModel):
    copy: Any
    fit_intercept: Any
    normalize: Any
    max_iter: Any
    cv: Any
    n_jobs: Any
    verbose: Any
    def __init__(self, *, copy: bool = ..., fit_intercept: bool = ..., normalize: str = ..., max_iter: Any | None = ..., cv: Any | None = ..., n_jobs: Any | None = ..., verbose: bool = ...) -> None: ...
    n_nonzero_coefs_: Any
    coef_: Any
    intercept_: Any
    n_iter_: Any
    def fit(self, X, y): ...
