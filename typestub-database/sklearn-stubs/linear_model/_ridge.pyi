from ..base import MultiOutputMixin as MultiOutputMixin, RegressorMixin as RegressorMixin, is_classifier as is_classifier
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics import check_scoring as check_scoring
from ..model_selection import GridSearchCV as GridSearchCV
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils import check_array as check_array, check_consistent_length as check_consistent_length, column_or_1d as column_or_1d, compute_sample_weight as compute_sample_weight
from ..utils.extmath import row_norms as row_norms, safe_sparse_dot as safe_sparse_dot
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import LinearClassifierMixin as LinearClassifierMixin, LinearModel as LinearModel
from ._sag import sag_solver as sag_solver
from abc import ABCMeta, abstractmethod
from scipy import sparse
from typing import Any

def ridge_regression(X, y, alpha, *, sample_weight: Any | None = ..., solver: str = ..., max_iter: Any | None = ..., tol: float = ..., verbose: int = ..., positive: bool = ..., random_state: Any | None = ..., return_n_iter: bool = ..., return_intercept: bool = ..., check_input: bool = ...): ...

class _BaseRidge(LinearModel, metaclass=ABCMeta):
    alpha: Any
    fit_intercept: Any
    normalize: Any
    copy_X: Any
    max_iter: Any
    tol: Any
    solver: Any
    positive: Any
    random_state: Any
    @abstractmethod
    def __init__(self, alpha: float = ..., *, fit_intercept: bool = ..., normalize: str = ..., copy_X: bool = ..., max_iter: Any | None = ..., tol: float = ..., solver: str = ..., positive: bool = ..., random_state: Any | None = ...): ...
    def fit(self, X, y, sample_weight: Any | None = ...): ...

class Ridge(MultiOutputMixin, RegressorMixin, _BaseRidge):
    def __init__(self, alpha: float = ..., *, fit_intercept: bool = ..., normalize: str = ..., copy_X: bool = ..., max_iter: Any | None = ..., tol: float = ..., solver: str = ..., positive: bool = ..., random_state: Any | None = ...) -> None: ...
    def fit(self, X, y, sample_weight: Any | None = ...): ...

class _RidgeClassifierMixin(LinearClassifierMixin):
    def predict(self, X): ...
    @property
    def classes_(self): ...

class RidgeClassifier(_RidgeClassifierMixin, _BaseRidge):
    class_weight: Any
    def __init__(self, alpha: float = ..., *, fit_intercept: bool = ..., normalize: str = ..., copy_X: bool = ..., max_iter: Any | None = ..., tol: float = ..., class_weight: Any | None = ..., solver: str = ..., positive: bool = ..., random_state: Any | None = ...) -> None: ...
    def fit(self, X, y, sample_weight: Any | None = ...): ...

class _X_CenterStackOp(sparse.linalg.LinearOperator):
    X: Any
    X_mean: Any
    sqrt_sw: Any
    def __init__(self, X, X_mean, sqrt_sw) -> None: ...

class _XT_CenterStackOp(sparse.linalg.LinearOperator):
    X: Any
    X_mean: Any
    sqrt_sw: Any
    def __init__(self, X, X_mean, sqrt_sw) -> None: ...

class _IdentityRegressor:
    def decision_function(self, y_predict): ...
    def predict(self, y_predict): ...

class _IdentityClassifier(LinearClassifierMixin):
    classes_: Any
    def __init__(self, classes) -> None: ...
    def decision_function(self, y_predict): ...

class _RidgeGCV(LinearModel):
    alphas: Any
    fit_intercept: Any
    normalize: Any
    scoring: Any
    copy_X: Any
    gcv_mode: Any
    store_cv_values: Any
    is_clf: Any
    alpha_per_target: Any
    def __init__(self, alphas=..., *, fit_intercept: bool = ..., normalize: str = ..., scoring: Any | None = ..., copy_X: bool = ..., gcv_mode: Any | None = ..., store_cv_values: bool = ..., is_clf: bool = ..., alpha_per_target: bool = ...) -> None: ...
    cv_values_: Any
    alpha_: Any
    best_score_: Any
    dual_coef_: Any
    coef_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...

class _BaseRidgeCV(LinearModel):
    alphas: Any
    fit_intercept: Any
    normalize: Any
    scoring: Any
    cv: Any
    gcv_mode: Any
    store_cv_values: Any
    alpha_per_target: Any
    def __init__(self, alphas=..., *, fit_intercept: bool = ..., normalize: str = ..., scoring: Any | None = ..., cv: Any | None = ..., gcv_mode: Any | None = ..., store_cv_values: bool = ..., alpha_per_target: bool = ...) -> None: ...
    alpha_: Any
    best_score_: Any
    cv_values_: Any
    coef_: Any
    intercept_: Any
    n_features_in_: Any
    feature_names_in_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...

class RidgeCV(MultiOutputMixin, RegressorMixin, _BaseRidgeCV): ...

class RidgeClassifierCV(_RidgeClassifierMixin, _BaseRidgeCV):
    class_weight: Any
    def __init__(self, alphas=..., *, fit_intercept: bool = ..., normalize: str = ..., scoring: Any | None = ..., cv: Any | None = ..., class_weight: Any | None = ..., store_cv_values: bool = ...) -> None: ...
    def fit(self, X, y, sample_weight: Any | None = ...): ...
