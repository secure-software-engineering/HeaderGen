from statsmodels.base.model import Model as Model
from statsmodels.compat.pandas import Substitution as Substitution
from statsmodels.iolib import summary2 as summary2
from typing import Any

__docformat__: str

def multivariate_stats(eigenvals, r_err_sscp, r_contrast, df_resid, tolerance: float = ...): ...

class _MultivariateOLS(Model):
    def __init__(self, endog, exog, missing: str = ..., hasconst: Any | None = ..., **kwargs) -> None: ...
    def fit(self, method: str = ...): ...

class _MultivariateOLSResults:
    design_info: Any
    exog_names: Any
    endog_names: Any
    def __init__(self, fitted_mv_ols) -> None: ...
    def mv_test(self, hypotheses: Any | None = ...): ...
    def summary(self) -> None: ...

class MultivariateTestResults:
    results: Any
    endog_names: Any
    exog_names: Any
    def __init__(self, results, endog_names, exog_names) -> None: ...
    def __getitem__(self, item): ...
    @property
    def summary_frame(self): ...
    def summary(self, show_contrast_L: bool = ..., show_transform_M: bool = ..., show_constant_C: bool = ...): ...
