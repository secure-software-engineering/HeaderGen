from sklearn import config_context as config_context
from sklearn.exceptions import DataConversionWarning as DataConversionWarning
from sklearn.metrics.pairwise import PAIRED_DISTANCES as PAIRED_DISTANCES, PAIRWISE_BOOLEAN_FUNCTIONS as PAIRWISE_BOOLEAN_FUNCTIONS, PAIRWISE_DISTANCE_FUNCTIONS as PAIRWISE_DISTANCE_FUNCTIONS, PAIRWISE_KERNEL_FUNCTIONS as PAIRWISE_KERNEL_FUNCTIONS, additive_chi2_kernel as additive_chi2_kernel, check_paired_arrays as check_paired_arrays, check_pairwise_arrays as check_pairwise_arrays, chi2_kernel as chi2_kernel, cosine_distances as cosine_distances, cosine_similarity as cosine_similarity, euclidean_distances as euclidean_distances, haversine_distances as haversine_distances, laplacian_kernel as laplacian_kernel, linear_kernel as linear_kernel, manhattan_distances as manhattan_distances, nan_euclidean_distances as nan_euclidean_distances, paired_distances as paired_distances, paired_euclidean_distances as paired_euclidean_distances, paired_manhattan_distances as paired_manhattan_distances, pairwise_distances as pairwise_distances, pairwise_distances_argmin as pairwise_distances_argmin, pairwise_distances_argmin_min as pairwise_distances_argmin_min, pairwise_distances_chunked as pairwise_distances_chunked, pairwise_kernels as pairwise_kernels, polynomial_kernel as polynomial_kernel, rbf_kernel as rbf_kernel, sigmoid_kernel as sigmoid_kernel
from sklearn.preprocessing import normalize as normalize
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_equal as assert_array_equal, ignore_warnings as ignore_warnings
from sklearn.utils.fixes import parse_version as parse_version, sp_version as sp_version

def test_pairwise_distances() -> None: ...
def test_pairwise_boolean_distance(metric) -> None: ...
def test_no_data_conversion_warning() -> None: ...
def test_pairwise_precomputed(func) -> None: ...
def test_pairwise_precomputed_non_negative() -> None: ...
def callable_rbf_kernel(x, y, **kwds): ...
def test_pairwise_parallel(func, metric, kwds, dtype) -> None: ...
def test_pairwise_callable_nonstrict_metric(): ...
def test_pairwise_kernels(metric) -> None: ...
def test_pairwise_kernels_callable() -> None: ...
def test_pairwise_kernels_filter_param() -> None: ...
def test_paired_distances(metric, func) -> None: ...
def test_paired_distances_callable(): ...
def test_pairwise_distances_argmin_min() -> None: ...
def test_pairwise_distances_chunked_reduce() -> None: ...
def test_pairwise_distances_chunked_reduce_none() -> None: ...
def test_pairwise_distances_chunked_reduce_valid(good_reduce) -> None: ...
def test_pairwise_distances_chunked_reduce_invalid(bad_reduce, err_type, message) -> None: ...
def check_pairwise_distances_chunked(X, Y, working_memory, metric: str = ...) -> None: ...
def test_pairwise_distances_chunked_diagonal(metric) -> None: ...
def test_parallel_pairwise_distances_diagonal(metric) -> None: ...
def test_pairwise_distances_chunked() -> None: ...
def test_euclidean_distances_known_result(x_array_constr, y_array_constr) -> None: ...
def test_euclidean_distances_with_norms(dtype, y_array_constr) -> None: ...
def test_euclidean_distances_norm_shapes() -> None: ...
def test_euclidean_distances(dtype, x_array_constr, y_array_constr) -> None: ...
def test_euclidean_distances_sym(dtype, x_array_constr) -> None: ...
def test_euclidean_distances_upcast(batch_size, x_array_constr, y_array_constr) -> None: ...
def test_euclidean_distances_upcast_sym(batch_size, x_array_constr) -> None: ...
def test_euclidean_distances_extreme_values(dtype, eps, rtol, dim) -> None: ...
def test_nan_euclidean_distances_equal_to_euclidean_distance(squared) -> None: ...
def test_nan_euclidean_distances_infinite_values(X, Y) -> None: ...
def test_nan_euclidean_distances_2x2(X, X_diag, missing_value) -> None: ...
def test_nan_euclidean_distances_complete_nan(missing_value) -> None: ...
def test_nan_euclidean_distances_not_trival(missing_value) -> None: ...
def test_nan_euclidean_distances_one_feature_match_positive(missing_value) -> None: ...
def test_cosine_distances() -> None: ...
def test_haversine_distances(): ...
def test_paired_euclidean_distances() -> None: ...
def test_paired_manhattan_distances() -> None: ...
def test_chi_square_kernel() -> None: ...
def test_kernel_symmetry(kernel) -> None: ...
def test_kernel_sparse(kernel) -> None: ...
def test_linear_kernel() -> None: ...
def test_rbf_kernel() -> None: ...
def test_laplacian_kernel() -> None: ...
def test_pairwise_similarity_sparse_output(metric, pairwise_func) -> None: ...
def test_cosine_similarity() -> None: ...
def test_check_dense_matrices() -> None: ...
def test_check_XB_returned() -> None: ...
def test_check_different_dimensions() -> None: ...
def test_check_invalid_dimensions() -> None: ...
def test_check_sparse_arrays() -> None: ...
def tuplify(X): ...
def test_check_tuple_input() -> None: ...
def test_check_preserve_type() -> None: ...
def test_pairwise_distances_data_derived_params(n_jobs, metric, dist_function) -> None: ...
def test_pairwise_distances_data_derived_params_error(metric) -> None: ...
def test_numeric_pairwise_distances_datatypes(metric, dtype, y_is_x) -> None: ...
