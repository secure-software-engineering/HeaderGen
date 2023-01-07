from ..metrics.cluster import mutual_info_score as mutual_info_score
from ..neighbors import KDTree as KDTree, NearestNeighbors as NearestNeighbors
from ..preprocessing import scale as scale
from ..utils import check_random_state as check_random_state
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_X_y as check_X_y, check_array as check_array
from typing import Any

def mutual_info_regression(X, y, *, discrete_features: str = ..., n_neighbors: int = ..., copy: bool = ..., random_state: Any | None = ...): ...
def mutual_info_classif(X, y, *, discrete_features: str = ..., n_neighbors: int = ..., copy: bool = ..., random_state: Any | None = ...): ...
