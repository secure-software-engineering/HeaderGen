from .. import average_precision_score as average_precision_score, precision_recall_curve as precision_recall_curve
from ...utils import check_matplotlib_support as check_matplotlib_support, deprecated as deprecated
from .._classification import check_consistent_length as check_consistent_length
from sklearn.base import is_classifier as is_classifier
from typing import Any

class PrecisionRecallDisplay:
    estimator_name: Any
    precision: Any
    recall: Any
    average_precision: Any
    pos_label: Any
    def __init__(self, precision, recall, *, average_precision: Any | None = ..., estimator_name: Any | None = ..., pos_label: Any | None = ...) -> None: ...
    ax_: Any
    figure_: Any
    def plot(self, ax: Any | None = ..., *, name: Any | None = ..., **kwargs): ...
    @classmethod
    def from_estimator(cls, estimator, X, y, *, sample_weight: Any | None = ..., pos_label: Any | None = ..., response_method: str = ..., name: Any | None = ..., ax: Any | None = ..., **kwargs): ...
    @classmethod
    def from_predictions(cls, y_true, y_pred, *, sample_weight: Any | None = ..., pos_label: Any | None = ..., name: Any | None = ..., ax: Any | None = ..., **kwargs): ...

def plot_precision_recall_curve(estimator, X, y, *, sample_weight: Any | None = ..., response_method: str = ..., name: Any | None = ..., ax: Any | None = ..., pos_label: Any | None = ..., **kwargs): ...
