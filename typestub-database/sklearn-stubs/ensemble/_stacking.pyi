from ..base import ClassifierMixin as ClassifierMixin, RegressorMixin as RegressorMixin, TransformerMixin as TransformerMixin, clone as clone, is_classifier as is_classifier, is_regressor as is_regressor
from ..exceptions import NotFittedError as NotFittedError
from ..linear_model import LogisticRegression as LogisticRegression, RidgeCV as RidgeCV
from ..model_selection import check_cv as check_cv, cross_val_predict as cross_val_predict
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils import Bunch as Bunch
from ..utils.fixes import delayed as delayed
from ..utils.metaestimators import if_delegate_has_method as if_delegate_has_method
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_is_fitted as check_is_fitted, column_or_1d as column_or_1d
from ._base import _BaseHeterogeneousEnsemble
from abc import ABCMeta, abstractmethod
from typing import Any

class _BaseStacking(TransformerMixin, _BaseHeterogeneousEnsemble, metaclass=ABCMeta):
    final_estimator: Any
    cv: Any
    stack_method: Any
    n_jobs: Any
    verbose: Any
    passthrough: Any
    @abstractmethod
    def __init__(self, estimators, final_estimator: Any | None = ..., *, cv: Any | None = ..., stack_method: str = ..., n_jobs: Any | None = ..., verbose: int = ..., passthrough: bool = ...): ...
    estimators_: Any
    named_estimators_: Any
    feature_names_in_: Any
    stack_method_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    @property
    def n_features_in_(self): ...
    def predict(self, X, **predict_params): ...

class StackingClassifier(ClassifierMixin, _BaseStacking):
    def __init__(self, estimators, final_estimator: Any | None = ..., *, cv: Any | None = ..., stack_method: str = ..., n_jobs: Any | None = ..., passthrough: bool = ..., verbose: int = ...) -> None: ...
    classes_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict(self, X, **predict_params): ...
    def predict_proba(self, X): ...
    def decision_function(self, X): ...
    def transform(self, X): ...

class StackingRegressor(RegressorMixin, _BaseStacking):
    def __init__(self, estimators, final_estimator: Any | None = ..., *, cv: Any | None = ..., n_jobs: Any | None = ..., passthrough: bool = ..., verbose: int = ...) -> None: ...
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def transform(self, X): ...
