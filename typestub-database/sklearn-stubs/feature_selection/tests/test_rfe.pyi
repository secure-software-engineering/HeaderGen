from sklearn.base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin
from sklearn.compose import TransformedTargetRegressor as TransformedTargetRegressor
from sklearn.datasets import load_iris as load_iris, make_friedman1 as make_friedman1
from sklearn.ensemble import RandomForestClassifier as RandomForestClassifier
from sklearn.feature_selection import RFE as RFE, RFECV as RFECV
from sklearn.linear_model import LogisticRegression as LogisticRegression
from sklearn.metrics import get_scorer as get_scorer, make_scorer as make_scorer, zero_one_loss as zero_one_loss
from sklearn.model_selection import GroupKFold as GroupKFold, cross_val_score as cross_val_score
from sklearn.pipeline import make_pipeline as make_pipeline
from sklearn.preprocessing import StandardScaler as StandardScaler
from sklearn.svm import LinearSVR as LinearSVR, SVC as SVC, SVR as SVR
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._testing import ignore_warnings as ignore_warnings
from typing import Any

class MockClassifier:
    foo_param: Any
    def __init__(self, foo_param: int = ...) -> None: ...
    coef_: Any
    def fit(self, X, y): ...
    def predict(self, T): ...
    predict_proba: Any
    decision_function: Any
    transform: Any
    def score(self, X: Any | None = ..., y: Any | None = ...): ...
    def get_params(self, deep: bool = ...): ...
    def set_params(self, **params): ...

def test_rfe_features_importance() -> None: ...
def test_rfe() -> None: ...
def test_RFE_fit_score_params(): ...
def test_rfe_invalid_n_features_errors(n_features_to_select) -> None: ...
def test_rfe_percent_n_features() -> None: ...
def test_rfe_mockclassifier() -> None: ...
def test_rfecv(): ...
def test_rfecv_mockclassifier() -> None: ...
def test_rfecv_verbose_output() -> None: ...
def test_rfecv_cv_results_size() -> None: ...
def test_rfe_estimator_tags() -> None: ...
def test_rfe_min_step() -> None: ...
def test_number_of_subsets_of_features(): ...
def test_rfe_cv_n_jobs() -> None: ...
def test_rfe_cv_groups() -> None: ...
def test_rfe_wrapped_estimator(importance_getter, selector, expected_n_features) -> None: ...
def test_rfe_importance_getter_validation(importance_getter, err_type, Selector) -> None: ...
def test_rfe_allow_nan_inf_in_x(cv) -> None: ...
def test_w_pipeline_2d_coef_() -> None: ...
def test_rfecv_std_and_mean() -> None: ...
def test_multioutput(ClsRFE) -> None: ...
