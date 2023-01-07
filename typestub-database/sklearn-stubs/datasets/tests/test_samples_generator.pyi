from sklearn.datasets import make_biclusters as make_biclusters, make_blobs as make_blobs, make_checkerboard as make_checkerboard, make_circles as make_circles, make_classification as make_classification, make_friedman1 as make_friedman1, make_friedman2 as make_friedman2, make_friedman3 as make_friedman3, make_hastie_10_2 as make_hastie_10_2, make_low_rank_matrix as make_low_rank_matrix, make_moons as make_moons, make_multilabel_classification as make_multilabel_classification, make_regression as make_regression, make_s_curve as make_s_curve, make_sparse_coded_signal as make_sparse_coded_signal, make_sparse_uncorrelated as make_sparse_uncorrelated, make_spd_matrix as make_spd_matrix, make_swiss_roll as make_swiss_roll
from sklearn.utils._testing import assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal
from sklearn.utils.validation import assert_all_finite as assert_all_finite

def test_make_classification() -> None: ...
def test_make_classification_informative_features() -> None: ...
def test_make_classification_weights_type(weights, err_type, err_msg) -> None: ...
def test_make_classification_weights_array_or_list_ok(kwargs) -> None: ...
def test_make_multilabel_classification_return_sequences() -> None: ...
def test_make_multilabel_classification_return_indicator() -> None: ...
def test_make_multilabel_classification_return_indicator_sparse() -> None: ...
def test_make_multilabel_classification_valid_arguments(params, err_msg) -> None: ...
def test_make_hastie_10_2() -> None: ...
def test_make_regression() -> None: ...
def test_make_regression_multitarget() -> None: ...
def test_make_blobs() -> None: ...
def test_make_blobs_n_samples_list() -> None: ...
def test_make_blobs_n_samples_list_with_centers() -> None: ...
def test_make_blobs_n_samples_centers_none(n_samples) -> None: ...
def test_make_blobs_return_centers() -> None: ...
def test_make_blobs_error() -> None: ...
def test_make_friedman1() -> None: ...
def test_make_friedman2() -> None: ...
def test_make_friedman3() -> None: ...
def test_make_low_rank_matrix() -> None: ...
def test_make_sparse_coded_signal() -> None: ...
def test_make_sparse_uncorrelated() -> None: ...
def test_make_spd_matrix() -> None: ...
def test_make_swiss_roll() -> None: ...
def test_make_s_curve() -> None: ...
def test_make_biclusters() -> None: ...
def test_make_checkerboard() -> None: ...
def test_make_moons() -> None: ...
def test_make_moons_unbalanced() -> None: ...
def test_make_circles() -> None: ...
def test_make_circles_unbalanced() -> None: ...
