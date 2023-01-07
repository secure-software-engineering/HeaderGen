from ..metrics import get_scorer as get_scorer
from ..model_selection import check_cv as check_cv
from ..preprocessing import LabelBinarizer as LabelBinarizer, LabelEncoder as LabelEncoder
from ..utils import check_array as check_array, check_consistent_length as check_consistent_length, check_random_state as check_random_state, compute_class_weight as compute_class_weight
from ..utils.extmath import log_logistic as log_logistic, row_norms as row_norms, safe_sparse_dot as safe_sparse_dot, softmax as softmax, squared_norm as squared_norm
from ..utils.fixes import delayed as delayed
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import BaseEstimator as BaseEstimator, LinearClassifierMixin as LinearClassifierMixin, SparseCoefMixin as SparseCoefMixin
from ._sag import sag_solver as sag_solver
from typing import Any

class LogisticRegression(LinearClassifierMixin, SparseCoefMixin, BaseEstimator):
    penalty: Any
    dual: Any
    tol: Any
    C: Any
    fit_intercept: Any
    intercept_scaling: Any
    class_weight: Any
    random_state: Any
    solver: Any
    max_iter: Any
    multi_class: Any
    verbose: Any
    warm_start: Any
    n_jobs: Any
    l1_ratio: Any
    def __init__(self, penalty: str = ..., *, dual: bool = ..., tol: float = ..., C: float = ..., fit_intercept: bool = ..., intercept_scaling: int = ..., class_weight: Any | None = ..., random_state: Any | None = ..., solver: str = ..., max_iter: int = ..., multi_class: str = ..., verbose: int = ..., warm_start: bool = ..., n_jobs: Any | None = ..., l1_ratio: Any | None = ...) -> None: ...
    classes_: Any
    n_iter_: Any
    coef_: Any
    intercept_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...

class LogisticRegressionCV(LogisticRegression, LinearClassifierMixin, BaseEstimator):
    Cs: Any
    fit_intercept: Any
    cv: Any
    dual: Any
    penalty: Any
    scoring: Any
    tol: Any
    max_iter: Any
    class_weight: Any
    n_jobs: Any
    verbose: Any
    solver: Any
    refit: Any
    intercept_scaling: Any
    multi_class: Any
    random_state: Any
    l1_ratios: Any
    def __init__(self, *, Cs: int = ..., fit_intercept: bool = ..., cv: Any | None = ..., dual: bool = ..., penalty: str = ..., scoring: Any | None = ..., solver: str = ..., tol: float = ..., max_iter: int = ..., class_weight: Any | None = ..., n_jobs: Any | None = ..., verbose: int = ..., refit: bool = ..., intercept_scaling: float = ..., multi_class: str = ..., random_state: Any | None = ..., l1_ratios: Any | None = ...) -> None: ...
    Cs_: Any
    n_iter_: Any
    scores_: Any
    coefs_paths_: Any
    C_: Any
    l1_ratio_: Any
    coef_: Any
    intercept_: Any
    l1_ratios_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def score(self, X, y, sample_weight: Any | None = ...): ...
