from typing import Any
import numpy

def cross_validate(
    estimator,
    X,
    y: Any | None = ...,
    *,
    groups: Any | None = ...,
    scoring: Any | None = ...,
    cv: Any | None = ...,
    n_jobs: Any | None = ...,
    verbose: int = ...,
    fit_params: Any | None = ...,
    pre_dispatch: str = ...,
    return_train_score: bool = ...,
    return_estimator: bool = ...,
    error_score=...
): ...
def cross_val_score(
    estimator,
    X,
    y: Any | None = ...,
    *,
    groups: Any | None = ...,
    scoring: Any | None = ...,
    cv: Any | None = ...,
    n_jobs: Any | None = ...,
    verbose: int = ...,
    fit_params: Any | None = ...,
    pre_dispatch: str = ...,
    error_score=...
) -> numpy.ndarray: ...
def cross_val_predict(
    estimator,
    X,
    y: Any | None = ...,
    *,
    groups: Any | None = ...,
    cv: Any | None = ...,
    n_jobs: Any | None = ...,
    verbose: int = ...,
    fit_params: Any | None = ...,
    pre_dispatch: str = ...,
    method: str = ...
) -> numpy.ndarray: ...
def permutation_test_score(
    estimator,
    X,
    y,
    *,
    groups: Any | None = ...,
    cv: Any | None = ...,
    n_permutations: int = ...,
    n_jobs: Any | None = ...,
    random_state: int = ...,
    verbose: int = ...,
    scoring: Any | None = ...,
    fit_params: Any | None = ...
): ...
def learning_curve(
    estimator,
    X,
    y,
    *,
    groups: Any | None = ...,
    train_sizes=...,
    cv: Any | None = ...,
    scoring: Any | None = ...,
    exploit_incremental_learning: bool = ...,
    n_jobs: Any | None = ...,
    pre_dispatch: str = ...,
    verbose: int = ...,
    shuffle: bool = ...,
    random_state: Any | None = ...,
    error_score=...,
    return_times: bool = ...,
    fit_params: Any | None = ...
): ...
def validation_curve(
    estimator,
    X,
    y,
    param_name,
    param_range,
    *,
    groups: Any | None = ...,
    cv: Any | None = ...,
    scoring: Any | None = ...,
    n_jobs: Any | None = ...,
    pre_dispatch: str = ...,
    verbose: int = ...,
    error_score=...,
    fit_params: Any | None = ...
): ...
