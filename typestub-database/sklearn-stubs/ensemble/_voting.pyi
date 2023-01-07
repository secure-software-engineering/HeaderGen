import abc
from ..base import ClassifierMixin as ClassifierMixin, RegressorMixin as RegressorMixin, TransformerMixin as TransformerMixin, clone as clone
from ..exceptions import NotFittedError as NotFittedError
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils import Bunch as Bunch
from ..utils.fixes import delayed as delayed
from ..utils.metaestimators import available_if as available_if
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_is_fitted as check_is_fitted, column_or_1d as column_or_1d
from ._base import _BaseHeterogeneousEnsemble
from abc import abstractmethod
from typing import Any

class _BaseVoting(TransformerMixin, _BaseHeterogeneousEnsemble, metaclass=abc.ABCMeta):
    estimators_: Any
    named_estimators_: Any
    feature_names_in_: Any
    @abstractmethod
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def fit_transform(self, X, y: Any | None = ..., **fit_params): ...
    @property
    def n_features_in_(self): ...

class VotingClassifier(ClassifierMixin, _BaseVoting):
    voting: Any
    weights: Any
    n_jobs: Any
    flatten_transform: Any
    verbose: Any
    def __init__(self, estimators, *, voting: str = ..., weights: Any | None = ..., n_jobs: Any | None = ..., flatten_transform: bool = ..., verbose: bool = ...) -> None: ...
    le_: Any
    classes_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def transform(self, X): ...

class VotingRegressor(RegressorMixin, _BaseVoting):
    weights: Any
    n_jobs: Any
    verbose: Any
    def __init__(self, estimators, *, weights: Any | None = ..., n_jobs: Any | None = ..., verbose: bool = ...) -> None: ...
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict(self, X): ...
    def transform(self, X): ...
