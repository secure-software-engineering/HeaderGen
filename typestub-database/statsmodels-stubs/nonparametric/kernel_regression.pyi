from ._kernel_base import GenericKDE
from typing import Any

class KernelReg(GenericKDE):
    var_type: Any
    data_type: Any
    reg_type: Any
    ckertype: Any
    okertype: Any
    ukertype: Any
    k_vars: Any
    endog: Any
    exog: Any
    data: Any
    nobs: Any
    est: Any
    bw: Any
    def __init__(self, endog, exog, var_type, reg_type: str = ..., bw: str = ..., ckertype: str = ..., okertype: str = ..., ukertype: str = ..., defaults: Any | None = ...) -> None: ...
    def aic_hurvich(self, bw, func: Any | None = ...): ...
    def cv_loo(self, bw, func): ...
    def r_squared(self): ...
    def fit(self, data_predict: Any | None = ...): ...
    def sig_test(self, var_pos, nboot: int = ..., nested_res: int = ..., pivot: bool = ...): ...

class KernelCensoredReg(KernelReg):
    var_type: Any
    data_type: Any
    reg_type: Any
    ckertype: Any
    okertype: Any
    ukertype: Any
    k_vars: Any
    endog: Any
    exog: Any
    data: Any
    nobs: Any
    est: Any
    censor_val: Any
    W_in: Any
    bw: Any
    def __init__(self, endog, exog, var_type, reg_type, bw: str = ..., ckertype: str = ..., ukertype: str = ..., okertype: str = ..., censor_val: int = ..., defaults: Any | None = ...) -> None: ...
    d: Any
    sortix: Any
    sortix_rev: Any
    def censored(self, censor_val) -> None: ...
    def cv_loo(self, bw, func): ...
    def fit(self, data_predict: Any | None = ...): ...

class TestRegCoefC:
    nboot: Any
    nres: Any
    test_vars: Any
    model: Any
    bw: Any
    var_type: Any
    k_vars: Any
    endog: Any
    exog: Any
    gx: Any
    pivot: Any
    def __init__(self, model, test_vars, nboot: int = ..., nested_res: int = ..., pivot: bool = ...) -> None: ...
    test_stat: Any
    sig: Any
    def run(self) -> None: ...

class TestRegCoefD(TestRegCoefC): ...
