from statsmodels.nonparametric.api import KernelReg
from typing import Any

class TestFForm:
    endog: Any
    exog: Any
    var_type: Any
    fform: Any
    estimator: Any
    nboot: Any
    bw: Any
    sig: Any
    def __init__(self, endog, exog, bw, var_type, fform, estimator, nboot: int = ...) -> None: ...

class SingleIndexModel(KernelReg):
    var_type: Any
    K: Any
    endog: Any
    exog: Any
    nobs: Any
    data_type: Any
    ckertype: str
    okertype: str
    ukertype: str
    func: Any
    def __init__(self, endog, exog, var_type) -> None: ...
    def cv_loo(self, params): ...
    def fit(self, data_predict: Any | None = ...): ...

class SemiLinear(KernelReg):
    endog: Any
    exog: Any
    K: Any
    exog_nonparametric: Any
    k_linear: Any
    nobs: Any
    var_type: Any
    data_type: Any
    ckertype: str
    okertype: str
    ukertype: str
    func: Any
    def __init__(self, endog, exog, exog_nonparametric, var_type, k_linear) -> None: ...
    def cv_loo(self, params): ...
    def fit(self, exog_predict: Any | None = ..., exog_nonparametric_predict: Any | None = ...): ...
