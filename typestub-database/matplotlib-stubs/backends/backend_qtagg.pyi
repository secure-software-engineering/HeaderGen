from .. import cbook as cbook
from .backend_agg import FigureCanvasAgg as FigureCanvasAgg
from .backend_qt import FigureCanvasQT as FigureCanvasQT, FigureManagerQT as FigureManagerQT, NavigationToolbar2QT as NavigationToolbar2QT, QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets, _BackendQT, backend_version as backend_version
from .qt_compat import QT_API as QT_API
from matplotlib.transforms import Bbox as Bbox
from typing import Any

class FigureCanvasQTAgg(FigureCanvasAgg, FigureCanvasQT):
    def __init__(self, figure: Any | None = ...) -> None: ...
    def paintEvent(self, event) -> None: ...
    def print_figure(self, *args, **kwargs) -> None: ...

class _BackendQTAgg(_BackendQT):
    FigureCanvas: Any
