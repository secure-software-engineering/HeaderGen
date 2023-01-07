from statsmodels.sandbox.tools import pca as pca
from statsmodels.sandbox.tools.cross_val import LeaveOneOut as LeaveOneOut
from typing import Any

class FactorModelUnivariate:
    endog: Any
    exog: Any
    def __init__(self, endog, exog) -> None: ...
    exog_reduced: Any
    factors: Any
    hasconst: int
    evals: Any
    evecs: Any
    def calc_factors(self, x: Any | None = ..., keepdim: int = ..., addconst: bool = ...) -> None: ...
    def fit_fixed_nfact(self, nfact): ...
    results_find_nfact: Any
    best_nfact: Any
    def fit_find_nfact(self, maxfact: Any | None = ..., skip_crossval: bool = ..., cv_iter: Any | None = ...) -> None: ...
    def summary_find_nfact(self): ...
