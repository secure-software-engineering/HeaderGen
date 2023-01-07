import statsmodels.base.wrapper as wrap
from statsmodels.base import model as model
from statsmodels.tools.sm_exceptions import ConvergenceWarning as ConvergenceWarning
from typing import Any

class _DimReductionRegression(model.Model):
    def __init__(self, endog, exog, **kwargs) -> None: ...

class SlicedInverseReg(_DimReductionRegression):
    def fit(self, slice_n: int = ..., **kwargs): ...
    ndim: Any
    k_vars: Any
    pen_mat: Any
    n_slice: Any
    def fit_regularized(self, ndim: int = ..., pen_mat: Any | None = ..., slice_n: int = ..., maxiter: int = ..., gtol: float = ..., **kwargs): ...

class PrincipalHessianDirections(_DimReductionRegression):
    def fit(self, **kwargs): ...

class SlicedAverageVarianceEstimation(_DimReductionRegression):
    bc: bool
    def __init__(self, endog, exog, **kwargs) -> None: ...
    def fit(self, **kwargs): ...

class DimReductionResults(model.Results):
    eigs: Any
    def __init__(self, model, params, eigs) -> None: ...

class DimReductionResultsWrapper(wrap.ResultsWrapper): ...

class CovarianceReduction(_DimReductionRegression):
    nobs: Any
    covm: Any
    covs: Any
    ns: Any
    dim: Any
    def __init__(self, endog, exog, dim) -> None: ...
    def loglike(self, params): ...
    def score(self, params): ...
    def fit(self, start_params: Any | None = ..., maxiter: int = ..., gtol: float = ...): ...
SIR = SlicedInverseReg
PHD = PrincipalHessianDirections
SAVE = SlicedAverageVarianceEstimation
CORE = CovarianceReduction
