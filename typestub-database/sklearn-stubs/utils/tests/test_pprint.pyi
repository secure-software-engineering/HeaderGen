from sklearn import config_context as config_context, set_config as set_config
from sklearn.base import BaseEstimator as BaseEstimator, TransformerMixin as TransformerMixin
from sklearn.feature_selection import SelectKBest as SelectKBest, chi2 as chi2
from sklearn.linear_model import LogisticRegressionCV as LogisticRegressionCV
from sklearn.pipeline import make_pipeline as make_pipeline
from typing import Any

class LogisticRegression(BaseEstimator):
    penalty: Any
    dual: Any
    tol: Any
    C: Any
    fit_intercept: Any
    intercept_scaling: Any
    class_weight: Any
    random_state: Any
    solver: Any
    max_iter: Any
    multi_class: Any
    verbose: Any
    warm_start: Any
    n_jobs: Any
    l1_ratio: Any
    def __init__(self, penalty: str = ..., dual: bool = ..., tol: float = ..., C: float = ..., fit_intercept: bool = ..., intercept_scaling: int = ..., class_weight: Any | None = ..., random_state: Any | None = ..., solver: str = ..., max_iter: int = ..., multi_class: str = ..., verbose: int = ..., warm_start: bool = ..., n_jobs: Any | None = ..., l1_ratio: Any | None = ...) -> None: ...
    def fit(self, X, y): ...

class StandardScaler(TransformerMixin, BaseEstimator):
    with_mean: Any
    with_std: Any
    copy: Any
    def __init__(self, copy: bool = ..., with_mean: bool = ..., with_std: bool = ...) -> None: ...
    def transform(self, X, copy: Any | None = ...): ...

class RFE(BaseEstimator):
    estimator: Any
    n_features_to_select: Any
    step: Any
    verbose: Any
    def __init__(self, estimator, n_features_to_select: Any | None = ..., step: int = ..., verbose: int = ...) -> None: ...

class GridSearchCV(BaseEstimator):
    estimator: Any
    param_grid: Any
    scoring: Any
    n_jobs: Any
    iid: Any
    refit: Any
    cv: Any
    verbose: Any
    pre_dispatch: Any
    error_score: Any
    return_train_score: Any
    def __init__(self, estimator, param_grid, scoring: Any | None = ..., n_jobs: Any | None = ..., iid: str = ..., refit: bool = ..., cv: str = ..., verbose: int = ..., pre_dispatch: str = ..., error_score: str = ..., return_train_score: bool = ...) -> None: ...

class CountVectorizer(BaseEstimator):
    input: Any
    encoding: Any
    decode_error: Any
    strip_accents: Any
    preprocessor: Any
    tokenizer: Any
    analyzer: Any
    lowercase: Any
    token_pattern: Any
    stop_words: Any
    max_df: Any
    min_df: Any
    max_features: Any
    ngram_range: Any
    vocabulary: Any
    binary: Any
    dtype: Any
    def __init__(self, input: str = ..., encoding: str = ..., decode_error: str = ..., strip_accents: Any | None = ..., lowercase: bool = ..., preprocessor: Any | None = ..., tokenizer: Any | None = ..., stop_words: Any | None = ..., token_pattern: str = ..., ngram_range=..., analyzer: str = ..., max_df: float = ..., min_df: int = ..., max_features: Any | None = ..., vocabulary: Any | None = ..., binary: bool = ..., dtype=...) -> None: ...

class Pipeline(BaseEstimator):
    steps: Any
    memory: Any
    def __init__(self, steps, memory: Any | None = ...) -> None: ...

class SVC(BaseEstimator):
    kernel: Any
    degree: Any
    gamma: Any
    coef0: Any
    tol: Any
    C: Any
    shrinking: Any
    probability: Any
    cache_size: Any
    class_weight: Any
    verbose: Any
    max_iter: Any
    decision_function_shape: Any
    random_state: Any
    def __init__(self, C: float = ..., kernel: str = ..., degree: int = ..., gamma: str = ..., coef0: float = ..., shrinking: bool = ..., probability: bool = ..., tol: float = ..., cache_size: int = ..., class_weight: Any | None = ..., verbose: bool = ..., max_iter: int = ..., decision_function_shape: str = ..., random_state: Any | None = ...) -> None: ...

class PCA(BaseEstimator):
    n_components: Any
    copy: Any
    whiten: Any
    svd_solver: Any
    tol: Any
    iterated_power: Any
    random_state: Any
    def __init__(self, n_components: Any | None = ..., copy: bool = ..., whiten: bool = ..., svd_solver: str = ..., tol: float = ..., iterated_power: str = ..., random_state: Any | None = ...) -> None: ...

class NMF(BaseEstimator):
    n_components: Any
    init: Any
    solver: Any
    beta_loss: Any
    tol: Any
    max_iter: Any
    random_state: Any
    alpha: Any
    l1_ratio: Any
    verbose: Any
    shuffle: Any
    def __init__(self, n_components: Any | None = ..., init: Any | None = ..., solver: str = ..., beta_loss: str = ..., tol: float = ..., max_iter: int = ..., random_state: Any | None = ..., alpha: float = ..., l1_ratio: float = ..., verbose: int = ..., shuffle: bool = ...) -> None: ...

class SimpleImputer(BaseEstimator):
    missing_values: Any
    strategy: Any
    fill_value: Any
    verbose: Any
    copy: Any
    def __init__(self, missing_values=..., strategy: str = ..., fill_value: Any | None = ..., verbose: int = ..., copy: bool = ...) -> None: ...

def test_basic(print_changed_only_false) -> None: ...
def test_changed_only() -> None: ...
def test_pipeline(print_changed_only_false) -> None: ...
def test_deeply_nested(print_changed_only_false) -> None: ...
def test_gridsearch(print_changed_only_false) -> None: ...
def test_gridsearch_pipeline(print_changed_only_false) -> None: ...
def test_n_max_elements_to_show(print_changed_only_false) -> None: ...
def test_bruteforce_ellipsis(print_changed_only_false) -> None: ...
def test_builtin_prettyprinter() -> None: ...
def test_kwargs_in_init(): ...
def test_complexity_print_changed_only(): ...
