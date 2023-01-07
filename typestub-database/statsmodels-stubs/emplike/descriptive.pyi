from statsmodels.graphics import utils as utils
from typing import Any

def DescStat(endog): ...

class _OptFuncts:
    def __init__(self, endog) -> None: ...

class DescStatUV(_OptFuncts):
    endog: Any
    nobs: Any
    def __init__(self, endog) -> None: ...
    mu0: Any
    def test_mean(self, mu0, return_weights: bool = ...): ...
    r0: Any
    def ci_mean(self, sig: float = ..., method: str = ..., epsilon=..., gamma_low=..., gamma_high=...): ...
    sig2_0: Any
    def test_var(self, sig2_0, return_weights: bool = ...): ...
    def ci_var(self, lower_bound: Any | None = ..., upper_bound: Any | None = ..., sig: float = ...): ...
    def plot_contour(self, mu_low, mu_high, var_low, var_high, mu_step, var_step, levs=...): ...
    skew0: Any
    def test_skew(self, skew0, return_weights: bool = ...): ...
    kurt0: Any
    def test_kurt(self, kurt0, return_weights: bool = ...): ...
    def test_joint_skew_kurt(self, skew0, kurt0, return_weights: bool = ...): ...
    def ci_skew(self, sig: float = ..., upper_bound: Any | None = ..., lower_bound: Any | None = ...): ...
    def ci_kurt(self, sig: float = ..., upper_bound: Any | None = ..., lower_bound: Any | None = ...): ...

class DescStatMV(_OptFuncts):
    endog: Any
    nobs: Any
    def __init__(self, endog) -> None: ...
    new_weights: Any
    def mv_test_mean(self, mu_array, return_weights: bool = ...): ...
    def mv_mean_contour(self, mu1_low, mu1_upp, mu2_low, mu2_upp, step1, step2, levs=..., var1_name: Any | None = ..., var2_name: Any | None = ..., plot_dta: bool = ...): ...
    def test_corr(self, corr0, return_weights: int = ...): ...
    r0: Any
    def ci_corr(self, sig: float = ..., upper_bound: Any | None = ..., lower_bound: Any | None = ...): ...
