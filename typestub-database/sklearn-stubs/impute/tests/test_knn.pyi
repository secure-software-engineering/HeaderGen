from sklearn import config_context as config_context
from sklearn.impute import KNNImputer as KNNImputer
from sklearn.metrics.pairwise import nan_euclidean_distances as nan_euclidean_distances, pairwise_distances as pairwise_distances
from sklearn.neighbors import KNeighborsRegressor as KNeighborsRegressor
from sklearn.utils._testing import assert_allclose as assert_allclose

def test_knn_imputer_shape(weights, n_neighbors) -> None: ...
def test_knn_imputer_default_with_invalid_input(na) -> None: ...
def test_knn_imputer_removes_all_na_features(na) -> None: ...
def test_knn_imputer_zero_nan_imputes_the_same(na) -> None: ...
def test_knn_imputer_verify(na) -> None: ...
def test_knn_imputer_one_n_neighbors(na) -> None: ...
def test_knn_imputer_all_samples_are_neighbors(na) -> None: ...
def test_knn_imputer_weight_uniform(na): ...
def test_knn_imputer_weight_distance(na) -> None: ...
def test_knn_imputer_callable_metric(): ...
def test_knn_imputer_with_simple_example(na, working_memory) -> None: ...
def test_knn_imputer_not_enough_valid_distances(na, weights) -> None: ...
def test_knn_imputer_drops_all_nan_features(na) -> None: ...
def test_knn_imputer_distance_weighted_not_enough_neighbors(na, working_memory) -> None: ...
def test_knn_tags(na, allow_nan) -> None: ...
