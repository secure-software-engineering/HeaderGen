from .descriptive import _OptFuncts
from statsmodels.regression.linear_model import OLS as OLS, WLS as WLS
from statsmodels.tools import add_constant as add_constant
from statsmodels.tools.sm_exceptions import IterationLimitWarning as IterationLimitWarning
from typing import Any

class OptAFT(_OptFuncts):
    def __init__(self) -> None: ...

class emplikeAFT:
    nobs: Any
    endog: Any
    exog: Any
    censors: Any
    nvar: Any
    uncens_nobs: Any
    uncens_endog: Any
    uncens_exog: Any
    def __init__(self, endog, exog, censors) -> None: ...
    def fit(self): ...
    def predict(self, params, endog: Any | None = ...): ...

class AFTResults(OptAFT):
    model: Any
    def __init__(self, model) -> None: ...
    def params(self): ...
    def test_beta(self, b0_vals, param_nums, ftol=..., maxiter: int = ..., print_weights: int = ...): ...
    r0: Any
    def ci_beta(self, param_num, beta_high, beta_low, sig: float = ...): ...
