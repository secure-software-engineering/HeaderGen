from statsmodels.base.model import LikelihoodModelResults as LikelihoodModelResults
from typing import Any

class BayesGaussMI:
    exog_names: Any
    data: Any
    mask: Any
    nobs: Any
    nvar: Any
    patterns: Any
    cov: Any
    mean: Any
    mean_prior: Any
    cov_prior: Any
    cov_prior_df: Any
    def __init__(self, data, mean_prior: Any | None = ..., cov_prior: Any | None = ..., cov_prior_df: int = ...) -> None: ...
    def update(self) -> None: ...
    def update_data(self) -> None: ...
    def update_mean(self) -> None: ...
    def update_cov(self) -> None: ...

class MI:
    imp: Any
    skip: Any
    model: Any
    formula: Any
    model_args_fn: Any
    model_kwds_fn: Any
    fit_args: Any
    fit_kwds: Any
    xfunc: Any
    nrep: Any
    def __init__(self, imp, model, model_args_fn: Any | None = ..., model_kwds_fn: Any | None = ..., formula: Any | None = ..., fit_args: Any | None = ..., fit_kwds: Any | None = ..., xfunc: Any | None = ..., burn: int = ..., nrep: int = ..., skip: int = ...): ...
    def fit(self, results_cb: Any | None = ...): ...

class MIResults(LikelihoodModelResults):
    mi: Any
    def __init__(self, mi, model, params, normalized_cov_params) -> None: ...
    def summary(self, title: Any | None = ..., alpha: float = ...): ...
