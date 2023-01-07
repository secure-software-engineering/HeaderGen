from .. import auc as auc, roc_curve as roc_curve
from ...utils import check_matplotlib_support as check_matplotlib_support, deprecated as deprecated
from typing import Any

class RocCurveDisplay:
    estimator_name: Any
    fpr: Any
    tpr: Any
    roc_auc: Any
    pos_label: Any
    def __init__(self, fpr, tpr, *, roc_auc: Any | None = ..., estimator_name: Any | None = ..., pos_label: Any | None = ...) -> None: ...
    ax_: Any
    figure_: Any
    def plot(self, ax: Any | None = ..., *, name: Any | None = ..., **kwargs): ...
    @classmethod
    def from_estimator(cls, estimator, X, y, *, sample_weight: Any | None = ..., drop_intermediate: bool = ..., response_method: str = ..., pos_label: Any | None = ..., name: Any | None = ..., ax: Any | None = ..., **kwargs): ...
    @classmethod
    def from_predictions(cls, y_true, y_pred, *, sample_weight: Any | None = ..., drop_intermediate: bool = ..., pos_label: Any | None = ..., name: Any | None = ..., ax: Any | None = ..., **kwargs): ...

def plot_roc_curve(estimator, X, y, *, sample_weight: Any | None = ..., drop_intermediate: bool = ..., response_method: str = ..., name: Any | None = ..., ax: Any | None = ..., pos_label: Any | None = ..., **kwargs): ...
