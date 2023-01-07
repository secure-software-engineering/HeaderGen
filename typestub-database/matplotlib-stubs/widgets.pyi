from . import backend_tools as backend_tools, cbook as cbook, colors as colors, ticker as ticker
from .lines import Line2D as Line2D
from .patches import Circle as Circle, Ellipse as Ellipse, Rectangle as Rectangle
from .transforms import TransformedPatchPath as TransformedPatchPath
from matplotlib import docstring as docstring
from typing import Any

class LockDraw:
    def __init__(self) -> None: ...
    def __call__(self, o) -> None: ...
    def release(self, o) -> None: ...
    def available(self, o): ...
    def isowner(self, o): ...
    def locked(self): ...

class Widget:
    drawon: bool
    eventson: bool
    def set_active(self, active) -> None: ...
    def get_active(self): ...
    active: Any
    def ignore(self, event): ...

class AxesWidget(Widget):
    cids: Any
    ax: Any
    canvas: Any
    def __init__(self, ax) -> None: ...
    def connect_event(self, event, callback) -> None: ...
    def disconnect_events(self) -> None: ...

class Button(AxesWidget):
    cnt: Any
    observers: Any
    label: Any
    color: Any
    hovercolor: Any
    def __init__(self, ax, label, image: Any | None = ..., color: str = ..., hovercolor: str = ...) -> None: ...
    def on_clicked(self, func): ...
    def disconnect(self, cid) -> None: ...

class SliderBase(AxesWidget):
    orientation: Any
    closedmin: Any
    closedmax: Any
    valmin: Any
    valmax: Any
    valstep: Any
    drag_active: bool
    valfmt: Any
    def __init__(self, ax, orientation, closedmin, closedmax, valmin, valmax, valfmt, dragging, valstep) -> None: ...
    def disconnect(self, cid) -> None: ...
    def reset(self) -> None: ...

class Slider(SliderBase):
    cnt: Any
    observers: Any
    slidermin: Any
    slidermax: Any
    val: Any
    valinit: Any
    track: Any
    poly: Any
    hline: Any
    vline: Any
    label: Any
    valtext: Any
    def __init__(self, ax, label, valmin, valmax, valinit: float = ..., valfmt: Any | None = ..., closedmin: bool = ..., closedmax: bool = ..., slidermin: Any | None = ..., slidermax: Any | None = ..., dragging: bool = ..., valstep: Any | None = ..., orientation: str = ..., *, initcolor: str = ..., track_color: str = ..., handle_style: Any | None = ..., **kwargs) -> None: ...
    def set_val(self, val) -> None: ...
    def on_changed(self, func): ...

class RangeSlider(SliderBase):
    val: Any
    valinit: Any
    track: Any
    poly: Any
    label: Any
    valtext: Any
    def __init__(self, ax, label, valmin, valmax, valinit: Any | None = ..., valfmt: Any | None = ..., closedmin: bool = ..., closedmax: bool = ..., dragging: bool = ..., valstep: Any | None = ..., orientation: str = ..., track_color: str = ..., handle_style: Any | None = ..., **kwargs) -> None: ...
    def set_min(self, min) -> None: ...
    def set_max(self, max) -> None: ...
    def set_val(self, val) -> None: ...
    def on_changed(self, func): ...

class CheckButtons(AxesWidget):
    cnt: Any
    observers: Any
    labels: Any
    lines: Any
    rectangles: Any
    def __init__(self, ax, labels, actives: Any | None = ...) -> None: ...
    def set_active(self, index) -> None: ...
    def get_status(self): ...
    def on_clicked(self, func): ...
    def disconnect(self, cid) -> None: ...

class TextBox(AxesWidget):
    cnt: Any
    change_observers: Any
    submit_observers: Any
    DIST_FROM_LEFT: Any
    label: Any
    text_disp: Any
    cursor_index: int
    cursor: Any
    color: Any
    hovercolor: Any
    capturekeystrokes: bool
    def __init__(self, ax, label, initial: str = ..., color: str = ..., hovercolor: str = ..., label_pad: float = ..., textalignment: str = ...) -> None: ...
    @property
    def text(self): ...
    def set_val(self, val) -> None: ...
    def begin_typing(self, x) -> None: ...
    def stop_typing(self) -> None: ...
    def position_cursor(self, x) -> None: ...
    def on_text_change(self, func): ...
    def on_submit(self, func): ...
    def disconnect(self, cid) -> None: ...

class RadioButtons(AxesWidget):
    activecolor: Any
    value_selected: Any
    labels: Any
    circles: Any
    def __init__(self, ax, labels, active: int = ..., activecolor: str = ...) -> None: ...
    cnt: Any
    observers: Any
    def set_active(self, index) -> None: ...
    def on_clicked(self, func): ...
    def disconnect(self, cid) -> None: ...

class SubplotTool(Widget):
    figure: Any
    targetfig: Any
    buttonreset: Any
    def __init__(self, targetfig, toolfig) -> None: ...

class Cursor(AxesWidget):
    visible: bool
    horizOn: Any
    vertOn: Any
    useblit: Any
    lineh: Any
    linev: Any
    background: Any
    needclear: bool
    def __init__(self, ax, horizOn: bool = ..., vertOn: bool = ..., useblit: bool = ..., **lineprops) -> None: ...
    def clear(self, event) -> None: ...
    def onmove(self, event) -> None: ...

class MultiCursor(Widget):
    canvas: Any
    axes: Any
    horizOn: Any
    vertOn: Any
    visible: bool
    useblit: Any
    background: Any
    needclear: bool
    vlines: Any
    hlines: Any
    def __init__(self, canvas, axes, useblit: bool = ..., horizOn: bool = ..., vertOn: bool = ..., **lineprops) -> None: ...
    def connect(self) -> None: ...
    def disconnect(self) -> None: ...
    def clear(self, event) -> None: ...
    def onmove(self, event) -> None: ...

class _SelectorWidget(AxesWidget):
    visible: bool
    onselect: Any
    useblit: Any
    state_modifier_keys: Any
    background: Any
    validButtons: Any
    def __init__(self, ax, onselect, useblit: bool = ..., button: Any | None = ..., state_modifier_keys: Any | None = ...) -> None: ...
    eventpress: Any
    eventrelease: Any
    state: Any
    def set_active(self, active) -> None: ...
    def update_background(self, event) -> None: ...
    def connect_default_events(self) -> None: ...
    def ignore(self, event): ...
    def update(self): ...
    def press(self, event): ...
    def release(self, event): ...
    def onmove(self, event): ...
    def on_scroll(self, event) -> None: ...
    def on_key_press(self, event) -> None: ...
    def on_key_release(self, event) -> None: ...
    def set_visible(self, visible) -> None: ...
    def clear(self) -> None: ...
    @property
    def artists(self): ...
    def set_props(self, **props) -> None: ...
    def set_handle_props(self, **handle_props) -> None: ...

class SpanSelector(_SelectorWidget):
    visible: bool
    onmove_callback: Any
    minspan: Any
    grab_range: Any
    drag_from_anywhere: Any
    ignore_event_outside: Any
    canvas: Any
    def __init__(self, ax, onselect, direction, minspan: int = ..., useblit: bool = ..., props: Any | None = ..., onmove_callback: Any | None = ..., interactive: bool = ..., button: Any | None = ..., handle_props: Any | None = ..., grab_range: int = ..., drag_from_anywhere: bool = ..., ignore_event_outside: bool = ...) -> None: ...
    rect: Any
    rectprops: Any
    active_handle: Any
    pressv: Any
    span_stays: Any
    prev: Any
    ax: Any
    def new_axes(self, ax) -> None: ...
    def connect_default_events(self) -> None: ...
    @property
    def direction(self): ...
    @direction.setter
    def direction(self, direction) -> None: ...
    @property
    def extents(self): ...
    @extents.setter
    def extents(self, extents) -> None: ...

class ToolLineHandles:
    ax: Any
    def __init__(self, ax, positions, direction, line_props: Any | None = ..., useblit: bool = ...) -> None: ...
    @property
    def artists(self): ...
    @property
    def positions(self): ...
    @property
    def direction(self): ...
    def set_data(self, positions) -> None: ...
    def set_visible(self, value) -> None: ...
    def set_animated(self, value) -> None: ...
    def remove(self) -> None: ...
    def closest(self, x, y): ...

class ToolHandles:
    ax: Any
    def __init__(self, ax, x, y, marker: str = ..., marker_props: Any | None = ..., useblit: bool = ...) -> None: ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def artists(self): ...
    def set_data(self, pts, y: Any | None = ...) -> None: ...
    def set_visible(self, val) -> None: ...
    def set_animated(self, val) -> None: ...
    def closest(self, x, y): ...

class RectangleSelector(_SelectorWidget):
    visible: bool
    drag_from_anywhere: Any
    ignore_event_outside: Any
    minspanx: Any
    minspany: Any
    spancoords: Any
    grab_range: Any
    def __init__(self, ax, onselect, drawtype: str = ..., minspanx: int = ..., minspany: int = ..., useblit: bool = ..., lineprops: Any | None = ..., props: Any | None = ..., spancoords: str = ..., button: Any | None = ..., grab_range: int = ..., handle_props: Any | None = ..., interactive: bool = ..., state_modifier_keys: Any | None = ..., drag_from_anywhere: bool = ..., ignore_event_outside: bool = ...) -> None: ...
    to_draw: Any
    drawtype: Any
    active_handle: Any
    interactive: Any
    maxdist: Any
    @property
    def corners(self): ...
    @property
    def edge_centers(self): ...
    @property
    def center(self): ...
    @property
    def extents(self): ...
    @extents.setter
    def extents(self, extents) -> None: ...
    draw_shape: Any
    @property
    def geometry(self): ...

class EllipseSelector(RectangleSelector):
    draw_shape: Any

class LassoSelector(_SelectorWidget):
    verts: Any
    def __init__(self, ax, onselect: Any | None = ..., useblit: bool = ..., props: Any | None = ..., button: Any | None = ...) -> None: ...
    def onpress(self, event) -> None: ...
    def onrelease(self, event) -> None: ...

class PolygonSelector(_SelectorWidget):
    grab_range: Any
    def __init__(self, ax, onselect, useblit: bool = ..., props: Any | None = ..., handle_props: Any | None = ..., grab_range: int = ...) -> None: ...
    line: Any
    vertex_select_radius: Any
    def onmove(self, event): ...
    @property
    def verts(self): ...

class Lasso(AxesWidget):
    useblit: Any
    background: Any
    verts: Any
    line: Any
    callback: Any
    def __init__(self, ax, xy, callback: Any | None = ..., useblit: bool = ...) -> None: ...
    def onrelease(self, event) -> None: ...
    def onmove(self, event) -> None: ...
