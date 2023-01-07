from .backend_cairo import FigureCanvasCairo as FigureCanvasCairo, RendererCairo as RendererCairo, cairo as cairo
from .backend_qt import FigureCanvasQT as FigureCanvasQT, QtCore as QtCore, QtGui as QtGui, _BackendQT
from .qt_compat import QT_API as QT_API
from typing import Any

class FigureCanvasQTCairo(FigureCanvasQT, FigureCanvasCairo):
    def __init__(self, figure: Any | None = ...) -> None: ...
    def draw(self) -> None: ...
    def paintEvent(self, event) -> None: ...

class _BackendQTCairo(_BackendQT):
    FigureCanvas: Any
