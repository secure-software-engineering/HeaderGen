import abc
from ._search import BaseSearchCV
from typing import Any

class _SubsampleMetaSplitter:
    base_cv: Any
    fraction: Any
    subsample_test: Any
    random_state: Any
    def __init__(self, base_cv, fraction, subsample_test, random_state) -> None: ...
    def split(self, X, y, groups: Any | None = ...) -> None: ...

class BaseSuccessiveHalving(BaseSearchCV, metaclass=abc.ABCMeta):
    random_state: Any
    max_resources: Any
    resource: Any
    factor: Any
    min_resources: Any
    aggressive_elimination: Any
    def __init__(self, estimator, *, scoring: Any | None = ..., n_jobs: Any | None = ..., refit: bool = ..., cv: int = ..., verbose: int = ..., random_state: Any | None = ..., error_score=..., return_train_score: bool = ..., max_resources: str = ..., min_resources: str = ..., resource: str = ..., factor: int = ..., aggressive_elimination: bool = ...) -> None: ...
    best_score_: Any
    def fit(self, X, y: Any | None = ..., groups: Any | None = ..., **fit_params): ...

class HalvingGridSearchCV(BaseSuccessiveHalving):
    param_grid: Any
    def __init__(self, estimator, param_grid, *, factor: int = ..., resource: str = ..., max_resources: str = ..., min_resources: str = ..., aggressive_elimination: bool = ..., cv: int = ..., scoring: Any | None = ..., refit: bool = ..., error_score=..., return_train_score: bool = ..., random_state: Any | None = ..., n_jobs: Any | None = ..., verbose: int = ...) -> None: ...

class HalvingRandomSearchCV(BaseSuccessiveHalving):
    param_distributions: Any
    n_candidates: Any
    def __init__(self, estimator, param_distributions, *, n_candidates: str = ..., factor: int = ..., resource: str = ..., max_resources: str = ..., min_resources: str = ..., aggressive_elimination: bool = ..., cv: int = ..., scoring: Any | None = ..., refit: bool = ..., error_score=..., return_train_score: bool = ..., random_state: Any | None = ..., n_jobs: Any | None = ..., verbose: int = ...) -> None: ...
