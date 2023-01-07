from sklearn.neighbors._ball_tree import BallTree as BallTree
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils.validation import check_array as check_array
from typing import Any

rng: Any
V_mahalanobis: Any
DIMENSION: int
METRICS: Any
DISCRETE_METRICS: Any
BOOLEAN_METRICS: Any

def brute_force_neighbors(X, Y, k, metric, **kwargs): ...
def test_ball_tree_query_metrics(metric, array_type) -> None: ...
def test_query_haversine() -> None: ...
def test_array_object_type() -> None: ...
