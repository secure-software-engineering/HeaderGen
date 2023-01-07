from ..base import BaseEstimator as BaseEstimator, MultiOutputMixin as MultiOutputMixin, is_classifier as is_classifier
from ..exceptions import DataConversionWarning as DataConversionWarning, EfficiencyWarning as EfficiencyWarning
from ..metrics import pairwise_distances_chunked as pairwise_distances_chunked
from ..metrics.pairwise import PAIRWISE_DISTANCE_FUNCTIONS as PAIRWISE_DISTANCE_FUNCTIONS
from ..utils import check_array as check_array, gen_even_slices as gen_even_slices
from ..utils.deprecation import deprecated as deprecated
from ..utils.fixes import delayed as delayed, parse_version as parse_version
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_is_fitted as check_is_fitted, check_non_negative as check_non_negative
from ._ball_tree import BallTree as BallTree
from ._kd_tree import KDTree as KDTree
from abc import ABCMeta, abstractmethod
from typing import Any

VALID_METRICS: Any
VALID_METRICS_SPARSE: Any

class NeighborsBase(MultiOutputMixin, BaseEstimator, metaclass=ABCMeta):
    n_neighbors: Any
    radius: Any
    algorithm: Any
    leaf_size: Any
    metric: Any
    metric_params: Any
    p: Any
    n_jobs: Any
    @abstractmethod
    def __init__(self, n_neighbors: Any | None = ..., radius: Any | None = ..., algorithm: str = ..., leaf_size: int = ..., metric: str = ..., p: int = ..., metric_params: Any | None = ..., n_jobs: Any | None = ...): ...

class KNeighborsMixin:
    def kneighbors(self, X: Any | None = ..., n_neighbors: Any | None = ..., return_distance: bool = ...): ...
    def kneighbors_graph(self, X: Any | None = ..., n_neighbors: Any | None = ..., mode: str = ...): ...

class RadiusNeighborsMixin:
    def radius_neighbors(self, X: Any | None = ..., radius: Any | None = ..., return_distance: bool = ..., sort_results: bool = ...): ...
    def radius_neighbors_graph(self, X: Any | None = ..., radius: Any | None = ..., mode: str = ..., sort_results: bool = ...): ...
