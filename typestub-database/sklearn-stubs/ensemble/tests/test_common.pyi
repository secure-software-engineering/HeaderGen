from sklearn.base import ClassifierMixin as ClassifierMixin, clone as clone, is_classifier as is_classifier
from sklearn.datasets import load_diabetes as load_diabetes, load_iris as load_iris, make_classification as make_classification, make_regression as make_regression
from sklearn.ensemble import RandomForestClassifier as RandomForestClassifier, RandomForestRegressor as RandomForestRegressor, StackingClassifier as StackingClassifier, StackingRegressor as StackingRegressor, VotingClassifier as VotingClassifier, VotingRegressor as VotingRegressor
from sklearn.impute import SimpleImputer as SimpleImputer
from sklearn.linear_model import LinearRegression as LinearRegression, LogisticRegression as LogisticRegression
from sklearn.pipeline import make_pipeline as make_pipeline
from sklearn.svm import LinearSVC as LinearSVC, LinearSVR as LinearSVR, SVC as SVC, SVR as SVR
from typing import Any

X: Any
y: Any
X_r: Any
y_r: Any

def test_ensemble_heterogeneous_estimators_behavior(X, y, estimator) -> None: ...
def test_ensemble_heterogeneous_estimators_type(Ensemble) -> None: ...
def test_ensemble_heterogeneous_estimators_name_validation(X, y, Ensemble) -> None: ...
def test_ensemble_heterogeneous_estimators_all_dropped(X, y, estimator) -> None: ...
def test_heterogeneous_ensemble_support_missing_values(Ensemble, Estimator, X, y) -> None: ...
