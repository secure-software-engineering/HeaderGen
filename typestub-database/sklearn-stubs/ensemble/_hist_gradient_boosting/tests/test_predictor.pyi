from sklearn.datasets import make_regression as make_regression
from sklearn.ensemble._hist_gradient_boosting._bitset import set_bitset_memoryview as set_bitset_memoryview, set_raw_bitset_from_binned_bitset as set_raw_bitset_from_binned_bitset
from sklearn.ensemble._hist_gradient_boosting.common import ALMOST_INF as ALMOST_INF, G_H_DTYPE as G_H_DTYPE, PREDICTOR_RECORD_DTYPE as PREDICTOR_RECORD_DTYPE, X_BINNED_DTYPE as X_BINNED_DTYPE, X_BITSET_INNER_DTYPE as X_BITSET_INNER_DTYPE, X_DTYPE as X_DTYPE
from sklearn.ensemble._hist_gradient_boosting.grower import TreeGrower as TreeGrower
from sklearn.ensemble._hist_gradient_boosting.predictor import TreePredictor as TreePredictor
from sklearn.metrics import r2_score as r2_score
from sklearn.model_selection import train_test_split as train_test_split
from typing import Any

n_threads: Any

def test_regression_dataset(n_bins) -> None: ...
def test_infinite_values_and_thresholds(num_threshold, expected_predictions) -> None: ...
def test_categorical_predictor(bins_go_left, expected_predictions) -> None: ...
