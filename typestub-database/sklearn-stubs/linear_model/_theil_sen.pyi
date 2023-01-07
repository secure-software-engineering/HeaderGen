from ..base import RegressorMixin as RegressorMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils import check_random_state as check_random_state
from ..utils.fixes import delayed as delayed
from ._base import LinearModel as LinearModel
from typing import Any

class TheilSenRegressor(RegressorMixin, LinearModel):
    fit_intercept: Any
    copy_X: Any
    max_subpopulation: Any
    n_subsamples: Any
    max_iter: Any
    tol: Any
    random_state: Any
    n_jobs: Any
    verbose: Any
    def __init__(self, *, fit_intercept: bool = ..., copy_X: bool = ..., max_subpopulation: float = ..., n_subsamples: Any | None = ..., max_iter: int = ..., tol: float = ..., random_state: Any | None = ..., n_jobs: Any | None = ..., verbose: bool = ...) -> None: ...
    breakdown_: Any
    intercept_: Any
    coef_: Any
    def fit(self, X, y): ...
