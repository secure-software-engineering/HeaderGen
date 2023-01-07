import statsmodels.tsa.base.tsa_model as tsbase
from statsmodels.tools.decorators import deprecated_alias as deprecated_alias
from statsmodels.tools.numdiff import approx_fprime as approx_fprime, approx_hess as approx_hess
from statsmodels.tsa.tsatools import rename_trend as rename_trend
from statsmodels.tsa.vector_ar.irf import IRAnalysis as IRAnalysis
from statsmodels.tsa.vector_ar.var_model import VARProcess as VARProcess, VARResults as VARResults
from typing import Any

def svar_ckerr(svar_type, A, B) -> None: ...

class SVAR(tsbase.TimeSeriesModel):
    y: Any
    neqs: Any
    svar_type: Any
    A_original: Any
    B_original: Any
    A_mask: Any
    B_mask: Any
    A: Any
    B: Any
    def __init__(self, endog, svar_type, dates: Any | None = ..., freq: Any | None = ..., A: Any | None = ..., B: Any | None = ..., missing: str = ...) -> None: ...
    nobs: Any
    def fit(self, A_guess: Any | None = ..., B_guess: Any | None = ..., maxlags: Any | None = ..., method: str = ..., ic: Any | None = ..., trend: str = ..., verbose: bool = ..., s_method: str = ..., solver: str = ..., override: bool = ..., maxiter: int = ..., maxfun: int = ...): ...
    def loglike(self, params): ...
    def score(self, AB_mask): ...
    def hessian(self, AB_mask): ...
    def check_order(self, J) -> None: ...
    def check_rank(self, J) -> None: ...

class SVARProcess(VARProcess):
    k_ar: Any
    neqs: Any
    coefs: Any
    intercept: Any
    sigma_u: Any
    A_solve: Any
    B_solve: Any
    names: Any
    def __init__(self, coefs, intercept, sigma_u, A_solve, B_solve, names: Any | None = ...) -> None: ...
    def orth_ma_rep(self, maxn: int = ..., P: Any | None = ...) -> None: ...
    def svar_ma_rep(self, maxn: int = ..., P: Any | None = ...): ...

class SVARResults(SVARProcess, VARResults):
    model: Any
    endog: Any
    endog_lagged: Any
    dates: Any
    nobs: Any
    k_trend: Any
    k_exog: Any
    trendorder: Any
    exog_names: Any
    params: Any
    sigma_u: Any
    A: Any
    B: Any
    A_mask: Any
    B_mask: Any
    def __init__(self, endog, endog_lagged, params, sigma_u, lag_order, A: Any | None = ..., B: Any | None = ..., A_mask: Any | None = ..., B_mask: Any | None = ..., model: Any | None = ..., trend: str = ..., names: Any | None = ..., dates: Any | None = ...) -> None: ...
    def irf(self, periods: int = ..., var_order: Any | None = ...): ...
    def sirf_errband_mc(self, orth: bool = ..., repl: int = ..., steps: int = ..., signif: float = ..., seed: Any | None = ..., burn: int = ..., cum: bool = ...): ...
