from statsmodels.regression.linear_model import OLS as OLS, RegressionResults as RegressionResults
from statsmodels.tools.tools import add_constant as add_constant
from typing import Any

class ELOriginRegress:
    endog: Any
    exog: Any
    nobs: Any
    nvar: Any
    def __init__(self, endog, exog) -> None: ...
    def fit(self): ...
    def predict(self, params, exog: Any | None = ...): ...

class OriginResults(RegressionResults):
    model: Any
    params: Any
    llr: Any
    llf_el: Any
    def __init__(self, model, params, est_llr, llf_el) -> None: ...
    def el_test(self, b0_vals, param_nums, method: str = ..., stochastic_exog: int = ..., return_weights: int = ...): ...
    def conf_int_el(self, param_num, upper_bound: Any | None = ..., lower_bound: Any | None = ..., sig: float = ..., method: str = ..., stochastic_exog: int = ...): ...
