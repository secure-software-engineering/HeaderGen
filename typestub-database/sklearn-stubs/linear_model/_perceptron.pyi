from ._stochastic_gradient import BaseSGDClassifier as BaseSGDClassifier
from typing import Any

class Perceptron(BaseSGDClassifier):
    def __init__(self, *, penalty: Any | None = ..., alpha: float = ..., l1_ratio: float = ..., fit_intercept: bool = ..., max_iter: int = ..., tol: float = ..., shuffle: bool = ..., verbose: int = ..., eta0: float = ..., n_jobs: Any | None = ..., random_state: int = ..., early_stopping: bool = ..., validation_fraction: float = ..., n_iter_no_change: int = ..., class_weight: Any | None = ..., warm_start: bool = ...) -> None: ...
