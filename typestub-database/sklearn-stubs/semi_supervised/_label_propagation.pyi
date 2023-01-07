from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics.pairwise import rbf_kernel as rbf_kernel
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_is_fitted as check_is_fitted
from abc import ABCMeta
from typing import Any

class BaseLabelPropagation(ClassifierMixin, BaseEstimator, metaclass=ABCMeta):
    max_iter: Any
    tol: Any
    kernel: Any
    gamma: Any
    n_neighbors: Any
    alpha: Any
    n_jobs: Any
    def __init__(self, kernel: str = ..., *, gamma: int = ..., n_neighbors: int = ..., alpha: int = ..., max_iter: int = ..., tol: float = ..., n_jobs: Any | None = ...) -> None: ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    X_: Any
    classes_: Any
    label_distributions_: Any
    transduction_: Any
    def fit(self, X, y): ...

class LabelPropagation(BaseLabelPropagation):
    def __init__(self, kernel: str = ..., *, gamma: int = ..., n_neighbors: int = ..., max_iter: int = ..., tol: float = ..., n_jobs: Any | None = ...) -> None: ...
    def fit(self, X, y): ...

class LabelSpreading(BaseLabelPropagation):
    def __init__(self, kernel: str = ..., *, gamma: int = ..., n_neighbors: int = ..., alpha: float = ..., max_iter: int = ..., tol: float = ..., n_jobs: Any | None = ...) -> None: ...
