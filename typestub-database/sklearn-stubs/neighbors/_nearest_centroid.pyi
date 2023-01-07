from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin
from ..metrics.pairwise import pairwise_distances as pairwise_distances
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.sparsefuncs import csc_median_axis_0 as csc_median_axis_0
from ..utils.validation import check_is_fitted as check_is_fitted
from typing import Any

class NearestCentroid(ClassifierMixin, BaseEstimator):
    metric: Any
    shrink_threshold: Any
    def __init__(self, metric: str = ..., *, shrink_threshold: Any | None = ...) -> None: ...
    classes_: Any
    centroids_: Any
    def fit(self, X, y): ...
    def predict(self, X): ...
