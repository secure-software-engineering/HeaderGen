from sklearn.base import clone as clone
from sklearn.datasets import make_classification as make_classification, make_regression as make_regression
from sklearn.ensemble import HistGradientBoostingClassifier as HistGradientBoostingClassifier, HistGradientBoostingRegressor as HistGradientBoostingRegressor
from sklearn.metrics import check_scoring as check_scoring
from typing import Any

X_classification: Any
y_classification: Any
X_regression: Any
y_regression: Any

def test_max_iter_with_warm_start_validation(GradientBoosting, X, y) -> None: ...
def test_warm_start_yields_identical_results(GradientBoosting, X, y) -> None: ...
def test_warm_start_max_depth(GradientBoosting, X, y) -> None: ...
def test_warm_start_early_stopping(GradientBoosting, X, y, scoring) -> None: ...
def test_warm_start_equal_n_estimators(GradientBoosting, X, y) -> None: ...
def test_warm_start_clear(GradientBoosting, X, y) -> None: ...
def test_random_seeds_warm_start(GradientBoosting, X, y, rng_type): ...
