from .. import det_curve as det_curve
from ...utils import check_matplotlib_support as check_matplotlib_support, deprecated as deprecated
from typing import Any

class DetCurveDisplay:
    fpr: Any
    fnr: Any
    estimator_name: Any
    pos_label: Any
    def __init__(self, fpr, fnr, *, estimator_name: Any | None = ..., pos_label: Any | None = ...) -> None: ...
    @classmethod
    def from_estimator(cls, estimator, X, y, *, sample_weight: Any | None = ..., response_method: str = ..., pos_label: Any | None = ..., name: Any | None = ..., ax: Any | None = ..., **kwargs): ...
    @classmethod
    def from_predictions(cls, y_true, y_pred, *, sample_weight: Any | None = ..., pos_label: Any | None = ..., name: Any | None = ..., ax: Any | None = ..., **kwargs): ...
    ax_: Any
    figure_: Any
    def plot(self, ax: Any | None = ..., *, name: Any | None = ..., **kwargs): ...

def plot_det_curve(estimator, X, y, *, sample_weight: Any | None = ..., response_method: str = ..., name: Any | None = ..., ax: Any | None = ..., pos_label: Any | None = ..., **kwargs): ...
