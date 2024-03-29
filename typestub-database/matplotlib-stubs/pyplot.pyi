from pathlib import Path
from typing import (
    Any,
    ByteString,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

import numpy as _np
import pandas as _pd
from typing_extensions import Literal

from .artist import Artist, Line2D, LineCollection, Rectangle
from .axes import Axes as Axes
from .axes import SubplotBase, _LegendLocation
from .backend_bases import MouseEvent
from .collections import PolyCollection, PathCollection
from .color import Normalize
from .font_manager import FontProperties
from .image import AxesImage
from .legend import Legend
from .patheffects import AbstractPathEffect
from .text import Text
from .transforms import Bbox, Transform

_T = TypeVar("_T")
Data = Union[
    float,  # represents both int and float
    _np.ndarray[_np.int8],
    _np.ndarray[_np.int16],
    _np.ndarray[_np.int32],
    _np.ndarray[_np.int64],
    _np.ndarray[_np.float32],
    _np.ndarray[_np.float64],
    Sequence[int],
    Sequence[float],
]
NumericArray = Union[
    _pd.Series[int],
    _pd.Series[float],
    _np.ndarray[_np.int8],
    _np.ndarray[_np.int16],
    _np.ndarray[_np.int32],
    _np.ndarray[_np.int64],
    _np.ndarray[_np.float32],
    _np.ndarray[_np.float64],
    Sequence[int],
    Sequence[float],
]
StrArray = Union[_pd.Series[str], _np.ndarray[_np.str_], Sequence[str]]
PaperType = Literal[
    "letter",
    "legal",
    "executive",
    "ledger",
    "a0",
    "a1",
    "a2",
    "a3",
    "a4",
    "a5",
    "a6",
    "a7",
    "a8",
    "a9",
    "a10",
    "b0",
    "b1",
    "b2",
    "b3",
    "b4",
    "b5",
    "b6",
    "b7",
    "b8",
    "b9",
    "b10",
]

class Figure:
    def savefig(
        self,
        fname: Union[str, Path],
        dpi: Optional[int] = ...,
        quality: Optional[int] = ...,
        optimize: bool = ...,
        progressive: bool = ...,
        facecolor: Optional[str] = ...,
        edgecolor: Optional[str] = ...,
        orientation: Literal["landscape", "portrait"] = ...,
        papertype: PaperType = ...,
        format: Literal[
            "eps",
            "jpeg",
            "jpg",
            "pdf",
            "pgf",
            "png",
            "ps",
            "raw",
            "rgba",
            "svg",
            "svgz",
            "tif",
            "tiff",
        ] = ...,
        transparent: bool = ...,
        bbox_inches: Optional[Union[Literal["tight"], Bbox]] = ...,
        pad_inches: Optional[int] = ...,
        bbox_extra_artists: Sequence[Artist] = ...,
        metadata: Union[Dict[str, Optional[str]], Dict[ByteString, ByteString]] = ...,
        #  TODO: expand pil kwargs
        pil_kwargs: Dict[str, Any] = ...,
    ) -> None: ...
    def tight_layout(
        self,
        pad: Optional[float] = ...,
        h_pad: Optional[float] = ...,
        w_pad: Optional[float] = ...,
    ) -> None: ...
    def suptitle(
        self,
        t: str,
        x: float = ...,
        y: float = ...,
        horizontalalignment: Literal["center", "left", "right"] = ...,
        fontsize: Optional[int] = ...,
    ) -> None: ...
    def add_subplot(
        self,
        nrows: int = ...,
        ncols: int = ...,
        index: int = ...,
        polar: bool = ...,
        sharex: Axes = ...,
        sharey: Axes = ...,
        label: str = ...,
        **kwargs: Any,
    ) -> SubplotBase: ...
    def legend(self, *args: Any, **kwargs: Any) -> Legend: ...
    def clf(self) -> None: ...

@overload
def subplots(
    *,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[float, float] = ...,
) -> Tuple[Figure, Axes]: ...
@overload
def subplots(
    nrows: int,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[float, float] = ...,
) -> Tuple[Figure, List[Axes]]: ...
@overload
def subplots(
    *,
    ncols: int,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[float, float] = ...,
) -> Tuple[Figure, List[Axes]]: ...
@overload
def subplots(
    nrows: int,
    ncols: int,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: Literal[True] = ...,
    dpi: int = ...,
    figsize: Tuple[float, float] = ...,
) -> Tuple[Figure, List[List[Axes]]]: ...
@overload
def subplots(
    nrows: int = ...,
    ncols: int = ...,
    *,
    squeeze: Literal[False],
    sharex: bool = ...,
    sharey: bool = ...,
    dpi: int = ...,
    figsize: Tuple[float, float] = ...,
) -> Tuple[Figure, List[List[Axes]]]: ...
def figure(
    num: Optional[Union[int, str]] = ...,
    figsize: Optional[Tuple[float, float]] = ...,
    dpi: Optional[int] = ...,
    facecolor: Optional[str] = ...,
    edgecolor: Optional[str] = ...,
    frameon: bool = ...,
    FigureClass: Type[Figure] = ...,
    clear: bool = ...,
) -> Figure: ...
def subplots_adjust(
    left: Optional[float] = ...,
    bottom: Optional[float] = ...,
    right: Optional[float] = ...,
    top: Optional[float] = ...,
    wspace: Optional[float] = ...,
    hspace: Optional[float] = ...,
) -> None: ...
def close(fig: Union[None, Figure, Literal["all"]] = ...) -> None: ...
def clf() -> None: ...
def plot(
    x: Data,
    y: Data,
    fmt: Optional[str] = ...,
    *,
    scalex: bool = ...,
    scaley: bool = ...,
    ___line2d_kwargs___,
) -> None: ...
def scatter(
    x: Data,
    y: Data,
    s: Optional[Union[float, Optional[NumericArray]]] = ...,
    c: Optional[str] = ...,
    cmap: Optional[str] = ...,
    norm: Optional[Normalize] = ...,
    vmin: Optional[float] = ...,
    vmax: Optional[float] = ...,
    marker: Optional[str] = ...,
    alpha: Optional[float] = ...,
    linewidths: Optional[float] = ...,
    verts: Optional[List[Tuple]] = ...,
    edgecolors: Optional[Union[Literal["face", "none"], str, Sequence[str]]] = ...,
    *,
    plotnonfinite: bool = ...,
    data: Optional[Data] = ...,
    label: str = ...,
) -> PathCollection: ...
def show() -> None: ...
def savefig(
    fname: Union[str, Path],
    dpi: Optional[int] = ...,
    quality: Optional[int] = ...,
    optimize: bool = ...,
    progressive: bool = ...,
    facecolor: Optional[str] = ...,
    edgecolor: Optional[str] = ...,
    orientation: Literal["landscape", "portrait"] = ...,
    papertype: PaperType = ...,
    format: Literal[
        "eps", "jpeg", "jpg", "pdf", "pgf", "png", "ps", "raw", "rgba", "svg", "svgz", "tif", "tiff"
    ] = ...,
    transparent: bool = ...,
    bbox_inches: Optional[Union[Literal["tight"], Bbox]] = ...,
    pad_inches: Optional[int] = ...,
    bbox_extra_artists: Sequence[Artist] = ...,
    metadata: Union[Dict[str, Optional[str]], Dict[ByteString, ByteString]] = ...,
    #  TODO: expand pil kwargs
    pil_kwargs: Dict[str, Any] = ...,
) -> None: ...
def xlim(
    left: float = ...,
    right: float = ...,
    emit: bool = ...,
    auto: Optional[bool] = ...,
    xmin: float = ...,
    xmax: float = ...,
) -> Tuple[float, float]: ...
def ylim(
    bottom: float = ...,
    top: float = ...,
    emit: bool = ...,
    auto: Optional[bool] = ...,
    ymin: float = ...,
    ymax: float = ...,
) -> Tuple[float, float]: ...
def xticks(
    ticks: Optional[NumericArray] = ...,
    labels: Optional[StrArray] = ...,
    *,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    minor: bool = ...,
    ___text_kwargs___,
) -> Tuple[List[float], List[str]]: ...
def yticks(
    ticks: Optional[NumericArray] = ...,
    labels: Optional[StrArray] = ...,
    *,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    minor: bool = ...,
    ___text_kwargs___,
) -> Tuple[List[float], List[str]]: ...
def xlabel(
    ylabel: str,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    labelpad: Optional[float] = ...,
) -> str: ...
def ylabel(
    ylabel: str,
    fontdict: Optional[Dict[str, Union[str, int]]] = ...,
    labelpad: Optional[float] = ...,
) -> str: ...
def fill_between(
    x: NumericArray,
    y1: Union[NumericArray, float],
    y2: Union[NumericArray, float] = ...,
    where: Optional[List[bool]] = ...,
    interpolate: bool = ...,
    step: Optional[Literal["pre", "post", "mid"]] = ...,
    *,
    data: Optional[Data] = ...,
    #  TODO: Replace kwargs with PolygonCollection kwargs
    **kwargs: Any,
) -> PolyCollection: ...
def axhline(
    y: float = ..., xmin: float = ..., xmax: float = ...,
) -> Line2D: ...
def axvline(
    x: float = ..., ymin: float = ..., ymax: float = ..., ) -> Line2D: ...
def legend(
    handles: Sequence[Union[Artist, Tuple[Artist, ...]]] = ...,
    labels: Sequence[str] = ...,
    loc: _LegendLocation = ...,
    bbox_to_anchor: Tuple[float, float] = ...,
    ncol: int = ...,
) -> Legend: ...
def grid(
    b: Optional[bool] = ...,
    which: Literal["major", "minor", "both"] = ...,
    axis: Literal["both", "x", "y"] = ...,
) -> None: ...
def title(
    label: str,
    loc: Literal["left", "center", "right"] = ...,
    pad: Optional[float] = ...,
) -> None: ...
