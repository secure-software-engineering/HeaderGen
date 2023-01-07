from ..base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from ..linear_model import Lars as Lars, Lasso as Lasso, LassoLars as LassoLars, orthogonal_mp_gram as orthogonal_mp_gram
from ..utils import check_array as check_array, check_random_state as check_random_state, deprecated as deprecated, gen_batches as gen_batches, gen_even_slices as gen_even_slices
from ..utils.extmath import randomized_svd as randomized_svd, row_norms as row_norms, svd_flip as svd_flip
from ..utils.fixes import delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted
from typing import Any

def sparse_encode(X, dictionary, *, gram: Any | None = ..., cov: Any | None = ..., algorithm: str = ..., n_nonzero_coefs: Any | None = ..., alpha: Any | None = ..., copy_cov: bool = ..., init: Any | None = ..., max_iter: int = ..., n_jobs: Any | None = ..., check_input: bool = ..., verbose: int = ..., positive: bool = ...): ...
def dict_learning(X, n_components, alpha, *, max_iter: int = ..., tol: float = ..., method: str = ..., n_jobs: Any | None = ..., dict_init: Any | None = ..., code_init: Any | None = ..., callback: Any | None = ..., verbose: bool = ..., random_state: Any | None = ..., return_n_iter: bool = ..., positive_dict: bool = ..., positive_code: bool = ..., method_max_iter: int = ...): ...
def dict_learning_online(X, n_components: int = ..., *, alpha: int = ..., n_iter: int = ..., return_code: bool = ..., dict_init: Any | None = ..., callback: Any | None = ..., batch_size: int = ..., verbose: bool = ..., shuffle: bool = ..., n_jobs: Any | None = ..., method: str = ..., iter_offset: int = ..., random_state: Any | None = ..., return_inner_stats: bool = ..., inner_stats: Any | None = ..., return_n_iter: bool = ..., positive_dict: bool = ..., positive_code: bool = ..., method_max_iter: int = ...): ...

class _BaseSparseCoding(TransformerMixin):
    transform_algorithm: Any
    transform_n_nonzero_coefs: Any
    transform_alpha: Any
    transform_max_iter: Any
    split_sign: Any
    n_jobs: Any
    positive_code: Any
    def __init__(self, transform_algorithm, transform_n_nonzero_coefs, transform_alpha, split_sign, n_jobs, positive_code, transform_max_iter) -> None: ...
    def transform(self, X): ...

class SparseCoder(_BaseSparseCoding, BaseEstimator):
    dictionary: Any
    def __init__(self, dictionary, *, transform_algorithm: str = ..., transform_n_nonzero_coefs: Any | None = ..., transform_alpha: Any | None = ..., split_sign: bool = ..., n_jobs: Any | None = ..., positive_code: bool = ..., transform_max_iter: int = ...) -> None: ...
    def fit(self, X, y: Any | None = ...): ...
    @property
    def components_(self): ...
    def transform(self, X, y: Any | None = ...): ...
    @property
    def n_components_(self): ...
    @property
    def n_features_in_(self): ...

class DictionaryLearning(_BaseSparseCoding, BaseEstimator):
    n_components: Any
    alpha: Any
    max_iter: Any
    tol: Any
    fit_algorithm: Any
    code_init: Any
    dict_init: Any
    verbose: Any
    random_state: Any
    positive_dict: Any
    def __init__(self, n_components: Any | None = ..., *, alpha: int = ..., max_iter: int = ..., tol: float = ..., fit_algorithm: str = ..., transform_algorithm: str = ..., transform_n_nonzero_coefs: Any | None = ..., transform_alpha: Any | None = ..., n_jobs: Any | None = ..., code_init: Any | None = ..., dict_init: Any | None = ..., verbose: bool = ..., split_sign: bool = ..., random_state: Any | None = ..., positive_code: bool = ..., positive_dict: bool = ..., transform_max_iter: int = ...) -> None: ...
    components_: Any
    error_: Any
    def fit(self, X, y: Any | None = ...): ...

class MiniBatchDictionaryLearning(_BaseSparseCoding, BaseEstimator):
    n_components: Any
    alpha: Any
    n_iter: Any
    fit_algorithm: Any
    dict_init: Any
    verbose: Any
    shuffle: Any
    batch_size: Any
    split_sign: Any
    random_state: Any
    positive_dict: Any
    def __init__(self, n_components: Any | None = ..., *, alpha: int = ..., n_iter: int = ..., fit_algorithm: str = ..., n_jobs: Any | None = ..., batch_size: int = ..., shuffle: bool = ..., dict_init: Any | None = ..., transform_algorithm: str = ..., transform_n_nonzero_coefs: Any | None = ..., transform_alpha: Any | None = ..., verbose: bool = ..., split_sign: bool = ..., random_state: Any | None = ..., positive_code: bool = ..., positive_dict: bool = ..., transform_max_iter: int = ...) -> None: ...
    components_: Any
    inner_stats_: Any
    iter_offset_: Any
    random_state_: Any
    def fit(self, X, y: Any | None = ...): ...
    def partial_fit(self, X, y: Any | None = ..., iter_offset: Any | None = ...): ...
