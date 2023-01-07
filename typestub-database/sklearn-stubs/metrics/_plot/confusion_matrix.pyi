from .. import confusion_matrix as confusion_matrix
from ...base import is_classifier as is_classifier
from ...utils import check_matplotlib_support as check_matplotlib_support, deprecated as deprecated
from ...utils.multiclass import unique_labels as unique_labels
from typing import Any

class ConfusionMatrixDisplay:
    confusion_matrix: Any
    display_labels: Any
    def __init__(self, confusion_matrix, *, display_labels: Any | None = ...) -> None: ...
    im_: Any
    text_: Any
    figure_: Any
    ax_: Any
    def plot(self, *, include_values: bool = ..., cmap: str = ..., xticks_rotation: str = ..., values_format: Any | None = ..., ax: Any | None = ..., colorbar: bool = ...): ...
    @classmethod
    def from_estimator(cls, estimator, X, y, *, labels: Any | None = ..., sample_weight: Any | None = ..., normalize: Any | None = ..., display_labels: Any | None = ..., include_values: bool = ..., xticks_rotation: str = ..., values_format: Any | None = ..., cmap: str = ..., ax: Any | None = ..., colorbar: bool = ...): ...
    @classmethod
    def from_predictions(cls, y_true, y_pred, *, labels: Any | None = ..., sample_weight: Any | None = ..., normalize: Any | None = ..., display_labels: Any | None = ..., include_values: bool = ..., xticks_rotation: str = ..., values_format: Any | None = ..., cmap: str = ..., ax: Any | None = ..., colorbar: bool = ...): ...

def plot_confusion_matrix(estimator, X, y_true, *, labels: Any | None = ..., sample_weight: Any | None = ..., normalize: Any | None = ..., display_labels: Any | None = ..., include_values: bool = ..., xticks_rotation: str = ..., values_format: Any | None = ..., cmap: str = ..., ax: Any | None = ..., colorbar: bool = ...): ...
