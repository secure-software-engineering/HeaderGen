from statsmodels.base import model as model
from statsmodels.base.model import LikelihoodModelResults as LikelihoodModelResults, Model as Model
from statsmodels.compat.numpy import lstsq as lstsq
from statsmodels.compat.pandas import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly, call_cached_func as call_cached_func, get_cached_doc as get_cached_doc
from statsmodels.regression.linear_model import RegressionModel as RegressionModel, RegressionResults as RegressionResults
from statsmodels.tools.validation import array_like as array_like, int_like as int_like, string_like as string_like
from typing import Any, NamedTuple

def strip4(line): ...

class RollingStore(NamedTuple):
    params: Any
    ssr: Any
    llf: Any
    nobs: Any
    s2: Any
    xpxi: Any
    xeex: Any
    centered_tss: Any
    uncentered_tss: Any
common_params: Any
window_parameters: str
weight_parameters: str
extra_base: Any
extra_parameters: Any

class RollingWLS:
    k_constant: Any
    const_idx: Any
    def __init__(self, endog, exog, window: Any | None = ..., *, weights: Any | None = ..., min_nobs: Any | None = ..., missing: str = ..., expanding: bool = ...) -> None: ...
    def fit(self, method: str = ..., cov_type: str = ..., cov_kwds: Any | None = ..., reset: Any | None = ..., use_t: bool = ..., params_only: bool = ...): ...
    @classmethod
    def from_formula(cls, formula, data, window, weights: Any | None = ..., subset: Any | None = ..., *args, **kwargs): ...

class RollingOLS(RollingWLS):
    def __init__(self, endog, exog, window: Any | None = ..., *, min_nobs: Any | None = ..., missing: str = ..., expanding: bool = ...) -> None: ...

class RollingRegressionResults:
    model: Any
    def __init__(self, model, store: RollingStore, k_constant, use_t, cov_type) -> None: ...
    def aic(self): ...
    def bic(self): ...
    def info_criteria(self, crit, dk_params: int = ...): ...
    def params(self): ...
    def ssr(self): ...
    def llf(self): ...
    def df_model(self): ...
    def k_constant(self): ...
    def centered_tss(self): ...
    def uncentered_tss(self): ...
    def rsquared(self): ...
    def rsquared_adj(self): ...
    def nobs(self): ...
    def df_resid(self): ...
    def use_t(self): ...
    def ess(self): ...
    def mse_model(self): ...
    def mse_resid(self): ...
    def mse_total(self): ...
    def cov_params(self): ...
    def f_pvalue(self): ...
    def fvalue(self): ...
    def bse(self): ...
    def tvalues(self): ...
    def pvalues(self): ...
    def conf_int(self, alpha: float = ..., cols: Any | None = ...): ...
    @property
    def cov_type(self): ...
    @classmethod
    def load(cls, fname): ...
    remove_data: Any
    def save(self, fname, remove_data: bool = ...): ...
    def plot_recursive_coefficient(self, variables: Any | None = ..., alpha: float = ..., legend_loc: str = ..., fig: Any | None = ..., figsize: Any | None = ...): ...
