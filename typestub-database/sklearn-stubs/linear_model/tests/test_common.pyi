from sklearn.base import is_classifier as is_classifier
from sklearn.linear_model import ARDRegression as ARDRegression, BayesianRidge as BayesianRidge, LinearRegression as LinearRegression, Ridge as Ridge, RidgeCV as RidgeCV, RidgeClassifier as RidgeClassifier, RidgeClassifierCV as RidgeClassifierCV
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils.fixes import np_version as np_version, parse_version as parse_version

def test_linear_model_normalize_deprecation_message(estimator, normalize, n_warnings, warning_category) -> None: ...
