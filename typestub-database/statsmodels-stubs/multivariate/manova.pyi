from .multivariate_ols import MultivariateTestResults as MultivariateTestResults
from statsmodels.base.model import Model as Model
from statsmodels.compat.pandas import Substitution as Substitution
from typing import Any

__docformat__: str

class MANOVA(Model):
    def __init__(self, endog, exog, missing: str = ..., hasconst: Any | None = ..., **kwargs) -> None: ...
    def fit(self) -> None: ...
    def mv_test(self, hypotheses: Any | None = ...): ...
