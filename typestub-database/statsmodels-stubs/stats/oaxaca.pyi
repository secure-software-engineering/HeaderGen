from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.tools.tools import add_constant as add_constant
from typing import Any

class OaxacaBlinder:
    two_fold_type: Any
    bifurcate: Any
    cov_type: Any
    cov_kwds: Any
    neumark: Any
    exog: Any
    hasconst: Any
    bi_col: Any
    endog: Any
    gap: Any
    bi: Any
    exog_f_mean: Any
    exog_s_mean: Any
    def __init__(self, endog, exog, bifurcate, hasconst: bool = ..., swap: bool = ..., cov_type: str = ..., cov_kwds: Any | None = ...) -> None: ...
    def variance(self, decomp_type, n: int = ..., conf: float = ...): ...
    submitted_n: Any
    submitted_conf: Any
    submitted_weight: Any
    endow_eff: Any
    coef_eff: Any
    int_eff: Any
    def three_fold(self, std: bool = ..., n: Any | None = ..., conf: Any | None = ...): ...
    t_params: Any
    unexplained: Any
    explained: Any
    def two_fold(self, std: bool = ..., two_fold_type: str = ..., submitted_weight: Any | None = ..., n: Any | None = ..., conf: Any | None = ...): ...

class OaxacaResults:
    params: Any
    std: Any
    model_type: Any
    def __init__(self, results, model_type, std_val: Any | None = ...) -> None: ...
    def summary(self) -> None: ...
