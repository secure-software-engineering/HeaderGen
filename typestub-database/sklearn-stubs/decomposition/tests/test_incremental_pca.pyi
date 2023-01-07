from sklearn import datasets as datasets
from sklearn.decomposition import IncrementalPCA as IncrementalPCA, PCA as PCA
from sklearn.utils._testing import assert_allclose_dense_sparse as assert_allclose_dense_sparse, assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal
from typing import Any

iris: Any

def test_incremental_pca() -> None: ...
def test_incremental_pca_sparse(matrix_class) -> None: ...
def test_incremental_pca_check_projection() -> None: ...
def test_incremental_pca_inverse() -> None: ...
def test_incremental_pca_validation() -> None: ...
def test_n_components_none() -> None: ...
def test_incremental_pca_set_params() -> None: ...
def test_incremental_pca_num_features_change() -> None: ...
def test_incremental_pca_batch_signs() -> None: ...
def test_incremental_pca_batch_values() -> None: ...
def test_incremental_pca_batch_rank() -> None: ...
def test_incremental_pca_partial_fit() -> None: ...
def test_incremental_pca_against_pca_iris() -> None: ...
def test_incremental_pca_against_pca_random_data() -> None: ...
def test_explained_variances() -> None: ...
def test_singular_values() -> None: ...
def test_whitening() -> None: ...
def test_incremental_pca_partial_fit_float_division() -> None: ...
def test_incremental_pca_fit_overflow_error() -> None: ...
