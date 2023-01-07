from .base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin, MetaEstimatorMixin as MetaEstimatorMixin, RegressorMixin as RegressorMixin, clone as clone, is_classifier as is_classifier
from .isotonic import IsotonicRegression as IsotonicRegression
from .model_selection import check_cv as check_cv, cross_val_predict as cross_val_predict
from .preprocessing import LabelEncoder as LabelEncoder, label_binarize as label_binarize
from .svm import LinearSVC as LinearSVC
from .utils import check_matplotlib_support as check_matplotlib_support, column_or_1d as column_or_1d, deprecated as deprecated, indexable as indexable
from .utils.fixes import delayed as delayed
from .utils.multiclass import check_classification_targets as check_classification_targets
from .utils.validation import check_consistent_length as check_consistent_length, check_is_fitted as check_is_fitted
from typing import Any

class CalibratedClassifierCV(ClassifierMixin, MetaEstimatorMixin, BaseEstimator):
    base_estimator: Any
    method: Any
    cv: Any
    n_jobs: Any
    ensemble: Any
    def __init__(self, base_estimator: Any | None = ..., *, method: str = ..., cv: Any | None = ..., n_jobs: Any | None = ..., ensemble: bool = ...) -> None: ...
    calibrated_classifiers_: Any
    classes_: Any
    n_features_in_: Any
    feature_names_in_: Any
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict_proba(self, X): ...
    def predict(self, X): ...

class _CalibratedClassifier:
    base_estimator: Any
    calibrators: Any
    classes: Any
    method: Any
    def __init__(self, base_estimator, calibrators, classes, *, method: str = ...) -> None: ...
    @property
    def calibrators_(self): ...
    def predict_proba(self, X): ...

class _SigmoidCalibration(RegressorMixin, BaseEstimator):
    def fit(self, X, y, sample_weight: Any | None = ...): ...
    def predict(self, T): ...

def calibration_curve(y_true, y_prob, *, normalize: bool = ..., n_bins: int = ..., strategy: str = ...): ...

class CalibrationDisplay:
    prob_true: Any
    prob_pred: Any
    y_prob: Any
    estimator_name: Any
    def __init__(self, prob_true, prob_pred, y_prob, *, estimator_name: Any | None = ...) -> None: ...
    line_: Any
    ax_: Any
    figure_: Any
    def plot(self, *, ax: Any | None = ..., name: Any | None = ..., ref_line: bool = ..., **kwargs): ...
    @classmethod
    def from_estimator(cls, estimator, X, y, *, n_bins: int = ..., strategy: str = ..., name: Any | None = ..., ref_line: bool = ..., ax: Any | None = ..., **kwargs): ...
    @classmethod
    def from_predictions(cls, y_true, y_prob, *, n_bins: int = ..., strategy: str = ..., name: Any | None = ..., ref_line: bool = ..., ax: Any | None = ..., **kwargs): ...
