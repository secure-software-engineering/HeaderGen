from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.gaussian_process import GaussianProcessClassifier as GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF as RBF, WhiteKernel as WhiteKernel
from sklearn.gaussian_process.tests._mini_sequence_kernel import MiniSeqKernel as MiniSeqKernel
from sklearn.utils._testing import assert_almost_equal as assert_almost_equal, assert_array_equal as assert_array_equal
from typing import Any

def f(x): ...

X: Any
X2: Any
y: Any
fX: Any
y_mc: Any
fixed_kernel: Any
kernels: Any
non_fixed_kernels: Any

def test_predict_consistent(kernel) -> None: ...
def test_predict_consistent_structured() -> None: ...
def test_lml_improving(kernel) -> None: ...
def test_lml_precomputed(kernel) -> None: ...
def test_lml_without_cloning_kernel(kernel) -> None: ...
def test_converged_to_local_maximum(kernel) -> None: ...
def test_lml_gradient(kernel): ...
def test_random_starts() -> None: ...
def test_custom_optimizer(kernel): ...
def test_multi_class(kernel) -> None: ...
def test_multi_class_n_jobs(kernel) -> None: ...
def test_warning_bounds() -> None: ...
