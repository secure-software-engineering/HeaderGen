from ..._loss.glm_distribution import EDM_DISTRIBUTIONS as EDM_DISTRIBUTIONS, ExponentialDispersionModel as ExponentialDispersionModel, TweedieDistribution as TweedieDistribution
from ...base import BaseEstimator as BaseEstimator, RegressorMixin as RegressorMixin
from ...utils.validation import check_is_fitted as check_is_fitted
from .link import BaseLink as BaseLink, IdentityLink as IdentityLink, LogLink as LogLink
from typing import Any

class GeneralizedLinearRegressor(RegressorMixin, BaseEstimator):
    alpha: Any
    fit_intercept: Any
    family: Any
    link: Any
    solver: Any
    max_iter: Any
    tol: Any
    warm_start: Any
    verbose: Any
    def __init__(self, *, alpha: float = ..., fit_intercept: bool = ..., family: str = ..., link: str = ..., solver: str = ..., max_iter: int = ..., tol: float = ..., warm_start: bool = ..., verbose: int = ...) -> None: ...
    n_iter_: Any
    intercept_: Any
    coef_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict(self, X): ...
    def score(self, X, y, sample_weight: Any | None = ...): ...

class PoissonRegressor(GeneralizedLinearRegressor):
    def __init__(self, *, alpha: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., warm_start: bool = ..., verbose: int = ...) -> None: ...
    @property
    def family(self): ...
    @family.setter
    def family(self, value) -> None: ...

class GammaRegressor(GeneralizedLinearRegressor):
    def __init__(self, *, alpha: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., warm_start: bool = ..., verbose: int = ...) -> None: ...
    @property
    def family(self): ...
    @family.setter
    def family(self, value) -> None: ...

class TweedieRegressor(GeneralizedLinearRegressor):
    def __init__(self, *, power: float = ..., alpha: float = ..., fit_intercept: bool = ..., link: str = ..., max_iter: int = ..., tol: float = ..., warm_start: bool = ..., verbose: int = ...) -> None: ...
    @property
    def family(self): ...
    power: Any
    @family.setter
    def family(self, value) -> None: ...
