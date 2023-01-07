from statsmodels.regression.linear_model import GLS as GLS, OLS as OLS, WLS as WLS
from typing import Any

def atleast_2dcols(x): ...

class GLSHet2(GLS):
    exog_var: Any
    def __init__(self, endog, exog, exog_var, sigma: Any | None = ...) -> None: ...
    def fit(self, lambd: float = ...): ...

class GLSHet(WLS):
    exog_var: Any
    link: Any
    linkinv: Any
    def __init__(self, endog, exog, exog_var: Any | None = ..., weights: Any | None = ..., link: Any | None = ...): ...
    history: Any
    results_old: Any
    weights: Any
    def iterative_fit(self, maxiter: int = ...): ...
