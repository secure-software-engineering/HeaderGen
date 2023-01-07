import ast
from matplotlib import cbook as cbook
from matplotlib._enums import CapStyle as CapStyle, JoinStyle as JoinStyle
from matplotlib.cbook import ls_mapper as ls_mapper
from matplotlib.colors import Colormap as Colormap, is_color_like as is_color_like
from matplotlib.fontconfig_pattern import parse_fontconfig_pattern as parse_fontconfig_pattern
from typing import Any

interactive_bk: Any
non_interactive_bk: Any
all_backends: Any

class ValidateInStrings:
    key: Any
    ignorecase: Any
    valid: Any
    def __init__(self, key, valid, ignorecase: bool = ..., *, _deprecated_since: Any | None = ...): ...
    def __call__(self, s): ...

def validate_any(s): ...

validate_anylist: Any

def validate_bool(b): ...
def validate_axisbelow(s): ...
def validate_dpi(s): ...

validate_string: Any
validate_string_or_None: Any
validate_stringlist: Any
validate_int: Any
validate_int_or_None: Any
validate_float: Any
validate_float_or_None: Any
validate_floatlist: Any

def validate_fonttype(s): ...
def validate_backend(s): ...
def validate_color_or_inherit(s): ...
def validate_color_or_auto(s): ...
def validate_color_for_prop_cycle(s): ...
def validate_color(s): ...

validate_colorlist: Any

def validate_aspect(s): ...
def validate_fontsize_None(s): ...
def validate_fontsize(s): ...

validate_fontsizelist: Any

def validate_fontweight(s): ...
def validate_font_properties(s): ...
def validate_whiskers(s): ...
def validate_ps_distiller(s): ...

validate_fillstyle: Any
validate_fillstylelist: Any

def validate_markevery(s): ...

validate_markeverylist: Any

def validate_bbox(s): ...
def validate_sketch(s): ...
def validate_hatch(s): ...

validate_hatchlist: Any
validate_dashlist: Any

def cycler(*args, **kwargs): ...

class _DunderChecker(ast.NodeVisitor):
    def visit_Attribute(self, node) -> None: ...

def validate_cycler(s): ...
def validate_hist_bins(s): ...

class _ignorecase(list): ...
