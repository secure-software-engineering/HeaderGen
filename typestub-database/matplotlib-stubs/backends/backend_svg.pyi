from matplotlib import cbook as cbook
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, RendererBase as RendererBase, _Backend
from matplotlib.backends.backend_mixed import MixedModeRenderer as MixedModeRenderer
from matplotlib.colors import rgb2hex as rgb2hex
from matplotlib.dates import UTC as UTC
from matplotlib.mathtext import MathTextParser as MathTextParser
from matplotlib.path import Path as Path
from matplotlib.transforms import Affine2D as Affine2D, Affine2DBase as Affine2DBase
from typing import Any

backend_version: Any

def escape_cdata(s): ...
def escape_comment(s): ...
def escape_attrib(s): ...
def short_float_fmt(x): ...

class XMLWriter:
    def __init__(self, file) -> None: ...
    def start(self, tag, attrib=..., **extra): ...
    def comment(self, comment) -> None: ...
    def data(self, text) -> None: ...
    def end(self, tag: Any | None = ..., indent: bool = ...) -> None: ...
    def close(self, id) -> None: ...
    def element(self, tag, text: Any | None = ..., attrib=..., **extra) -> None: ...
    def flush(self) -> None: ...

def generate_transform(transform_list=...): ...
def generate_css(attrib=...): ...

class RendererSVG(RendererBase):
    width: Any
    height: Any
    writer: Any
    image_dpi: Any
    basename: Any
    def __init__(self, width, height, svgwriter, basename: Any | None = ..., image_dpi: int = ..., *, metadata: Any | None = ...) -> None: ...
    @property
    def mathtext_parser(self): ...
    def finalize(self) -> None: ...
    def open_group(self, s, gid: Any | None = ...) -> None: ...
    def close_group(self, s) -> None: ...
    def option_image_nocomposite(self): ...
    def draw_path(self, gc, path, transform, rgbFace: Any | None = ...) -> None: ...
    def draw_markers(self, gc, marker_path, marker_trans, path, trans, rgbFace: Any | None = ...) -> None: ...
    def draw_path_collection(self, gc, master_transform, paths, all_transforms, offsets, offsetTrans, facecolors, edgecolors, linewidths, linestyles, antialiaseds, urls, offset_position): ...
    def draw_gouraud_triangle(self, gc, points, colors, trans) -> None: ...
    def draw_gouraud_triangles(self, gc, triangles_array, colors_array, transform) -> None: ...
    def option_scale_image(self): ...
    def get_image_magnification(self): ...
    def draw_image(self, gc, x, y, im, transform: Any | None = ...) -> None: ...
    def draw_tex(self, gc, x, y, s, prop, angle, *, mtext: Any | None = ...) -> None: ...
    def draw_text(self, gc, x, y, s, prop, angle, ismath: bool = ..., mtext: Any | None = ...) -> None: ...
    def flipy(self): ...
    def get_canvas_width_height(self): ...
    def get_text_width_height_descent(self, s, prop, ismath): ...

class FigureCanvasSVG(FigureCanvasBase):
    filetypes: Any
    fixed_dpi: int
    def print_svg(self, filename, *args, dpi: Any | None = ..., bbox_inches_restore: Any | None = ..., metadata: Any | None = ...) -> None: ...
    def print_svgz(self, filename, *args, **kwargs): ...
    def get_default_filetype(self): ...
    def draw(self): ...
FigureManagerSVG = FigureManagerBase
svgProlog: str

class _BackendSVG(_Backend):
    FigureCanvas: Any
