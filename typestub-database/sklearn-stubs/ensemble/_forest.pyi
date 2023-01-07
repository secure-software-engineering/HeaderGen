from ..base import ClassifierMixin, MultiOutputMixin, RegressorMixin
from ._base import BaseEnsemble
from abc import ABCMeta, abstractmethod
from typing import Any

class BaseForest(MultiOutputMixin, BaseEnsemble, metaclass=ABCMeta):
    bootstrap: Any
    oob_score: Any
    n_jobs: Any
    random_state: Any
    verbose: Any
    warm_start: Any
    class_weight: Any
    max_samples: Any
    @abstractmethod
    def __init__(self, base_estimator, n_estimators: int = ..., *, estimator_params=..., bootstrap: bool = ..., oob_score: bool = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., verbose: int = ..., warm_start: bool = ..., class_weight: Any | None = ..., max_samples: Any | None = ...): ...
    def apply(self, X): ...
    def decision_path(self, X): ...
    n_outputs_: Any
    estimators_: Any
    n_classes_: Any
    classes_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    @property
    def feature_importances_(self): ...
    @property
    def n_features_(self): ...

class ForestClassifier(ClassifierMixin, BaseForest, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, base_estimator, n_estimators: int = ..., *, estimator_params=..., bootstrap: bool = ..., oob_score: bool = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., verbose: int = ..., warm_start: bool = ..., class_weight: Any | None = ..., max_samples: Any | None = ...): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...

class ForestRegressor(RegressorMixin, BaseForest, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, base_estimator, n_estimators: int = ..., *, estimator_params=..., bootstrap: bool = ..., oob_score: bool = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., verbose: int = ..., warm_start: bool = ..., max_samples: Any | None = ...): ...
    def predict(self, X): ...

class RandomForestClassifier(ForestClassifier):
    criterion: Any
    max_depth: Any
    min_samples_split: Any
    min_samples_leaf: Any
    min_weight_fraction_leaf: Any
    max_features: Any
    max_leaf_nodes: Any
    min_impurity_decrease: Any
    ccp_alpha: Any
    def __init__(self, n_estimators: int = ..., *, criterion: str = ..., max_depth: Any | None = ..., min_samples_split: int = ..., min_samples_leaf: int = ..., min_weight_fraction_leaf: float = ..., max_features: str = ..., max_leaf_nodes: Any | None = ..., min_impurity_decrease: float = ..., bootstrap: bool = ..., oob_score: bool = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., verbose: int = ..., warm_start: bool = ..., class_weight: Any | None = ..., ccp_alpha: float = ..., max_samples: Any | None = ...) -> None: ...

class RandomForestRegressor(ForestRegressor):
    criterion: Any
    max_depth: Any
    min_samples_split: Any
    min_samples_leaf: Any
    min_weight_fraction_leaf: Any
    max_features: Any
    max_leaf_nodes: Any
    min_impurity_decrease: Any
    ccp_alpha: Any
    def __init__(self, n_estimators: int = ..., *, criterion: str = ..., max_depth: Any | None = ..., min_samples_split: int = ..., min_samples_leaf: int = ..., min_weight_fraction_leaf: float = ..., max_features: str = ..., max_leaf_nodes: Any | None = ..., min_impurity_decrease: float = ..., bootstrap: bool = ..., oob_score: bool = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., verbose: int = ..., warm_start: bool = ..., ccp_alpha: float = ..., max_samples: Any | None = ...) -> None: ...

class ExtraTreesClassifier(ForestClassifier):
    criterion: Any
    max_depth: Any
    min_samples_split: Any
    min_samples_leaf: Any
    min_weight_fraction_leaf: Any
    max_features: Any
    max_leaf_nodes: Any
    min_impurity_decrease: Any
    ccp_alpha: Any
    def __init__(self, n_estimators: int = ..., *, criterion: str = ..., max_depth: Any | None = ..., min_samples_split: int = ..., min_samples_leaf: int = ..., min_weight_fraction_leaf: float = ..., max_features: str = ..., max_leaf_nodes: Any | None = ..., min_impurity_decrease: float = ..., bootstrap: bool = ..., oob_score: bool = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., verbose: int = ..., warm_start: bool = ..., class_weight: Any | None = ..., ccp_alpha: float = ..., max_samples: Any | None = ...) -> None: ...

class ExtraTreesRegressor(ForestRegressor):
    criterion: Any
    max_depth: Any
    min_samples_split: Any
    min_samples_leaf: Any
    min_weight_fraction_leaf: Any
    max_features: Any
    max_leaf_nodes: Any
    min_impurity_decrease: Any
    ccp_alpha: Any
    def __init__(self, n_estimators: int = ..., *, criterion: str = ..., max_depth: Any | None = ..., min_samples_split: int = ..., min_samples_leaf: int = ..., min_weight_fraction_leaf: float = ..., max_features: str = ..., max_leaf_nodes: Any | None = ..., min_impurity_decrease: float = ..., bootstrap: bool = ..., oob_score: bool = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., verbose: int = ..., warm_start: bool = ..., ccp_alpha: float = ..., max_samples: Any | None = ...) -> None: ...

class RandomTreesEmbedding(BaseForest):
    criterion: str
    max_features: int
    max_depth: Any
    min_samples_split: Any
    min_samples_leaf: Any
    min_weight_fraction_leaf: Any
    max_leaf_nodes: Any
    min_impurity_decrease: Any
    sparse_output: Any
    def __init__(self, n_estimators: int = ..., *, max_depth: int = ..., min_samples_split: int = ..., min_samples_leaf: int = ..., min_weight_fraction_leaf: float = ..., max_leaf_nodes: Any | None = ..., min_impurity_decrease: float = ..., sparse_output: bool = ..., n_jobs: Any | None = ..., random_state: Any | None = ..., verbose: int = ..., warm_start: bool = ...) -> None: ...
    def fit(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    one_hot_encoder_: Any
    def fit_transform(self, X, y: Any | None = ..., sample_weight: Any | None = ...): ...
    def transform(self, X): ...
