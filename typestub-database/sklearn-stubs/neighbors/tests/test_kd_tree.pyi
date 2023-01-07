from sklearn.neighbors._kd_tree import KDTree as KDTree
from sklearn.utils.fixes import delayed as delayed
from typing import Any

DIMENSION: int
METRICS: Any

def test_array_object_type() -> None: ...
def test_kdtree_picklable_with_joblib() -> None: ...
