from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.gaussian_process import GaussianProcessRegressor as GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct as DotProduct, ExpSineSquared as ExpSineSquared, RBF as RBF, WhiteKernel as WhiteKernel
from sklearn.gaussian_process.tests._mini_sequence_kernel import MiniSeqKernel as MiniSeqKernel
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_almost_equal as assert_almost_equal, assert_array_almost_equal as assert_array_almost_equal, assert_array_less as assert_array_less
from typing import Any

def f(x): ...

X: Any
X2: Any
y: Any
fixed_kernel: Any
kernels: Any
non_fixed_kernels: Any

def test_gpr_interpolation(kernel) -> None: ...
def test_gpr_interpolation_structured() -> None: ...
def test_lml_improving(kernel) -> None: ...
def test_lml_precomputed(kernel) -> None: ...
def test_lml_without_cloning_kernel(kernel) -> None: ...
def test_converged_to_local_maximum(kernel) -> None: ...
def test_solution_inside_bounds(kernel) -> None: ...
def test_lml_gradient(kernel): ...
def test_prior(kernel) -> None: ...
def test_sample_statistics(kernel) -> None: ...
def test_no_optimizer() -> None: ...
def test_predict_cov_vs_std(kernel, target) -> None: ...
def test_anisotropic_kernel() -> None: ...
def test_random_starts() -> None: ...
def test_y_normalization(kernel) -> None: ...
def test_large_variance_y() -> None: ...
def test_y_multioutput() -> None: ...
def test_custom_optimizer(kernel): ...
def test_gpr_correct_error_message() -> None: ...
def test_duplicate_input(kernel) -> None: ...
def test_no_fit_default_predict() -> None: ...
def test_warning_bounds() -> None: ...
def test_bound_check_fixed_hyperparameter() -> None: ...
def test_constant_target(kernel) -> None: ...
def test_gpr_consistency_std_cov_non_invertible_kernel() -> None: ...
def test_gpr_fit_error(params, TypeError, err_msg) -> None: ...
def test_gpr_lml_error() -> None: ...
def test_gpr_predict_error() -> None: ...
def test_y_std_with_multitarget_normalized() -> None: ...
