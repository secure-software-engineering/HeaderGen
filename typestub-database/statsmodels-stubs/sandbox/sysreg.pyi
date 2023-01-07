from statsmodels.base.model import LikelihoodModelResults
from typing import Any

class SUR:
    exog: Any
    endog: Any
    nobs: Any
    df_resid: Any
    df_model: Any
    sp_exog: Any
    sigma: Any
    cholsigmainv: Any
    def __init__(self, sys, sigma: Any | None = ..., dfk: Any | None = ...) -> None: ...
    wendog: Any
    wexog: Any
    pinv_wexog: Any
    normalized_cov_params: Any
    history: Any
    iterations: int
    def initialize(self) -> None: ...
    def whiten(self, X): ...
    def fit(self, igls: bool = ..., tol: float = ..., maxiter: int = ...): ...
    def predict(self, design) -> None: ...

class Sem2SLS:
    endog: Any
    exog: Any
    instruments: Any
    wexog: Any
    def __init__(self, sys, indep_endog: Any | None = ..., instruments: Any | None = ...) -> None: ...
    def whiten(self, Y): ...
    def fit(self): ...

class SysResults(LikelihoodModelResults):
    def __init__(self, model, params, normalized_cov_params: Any | None = ..., scale: float = ...) -> None: ...
