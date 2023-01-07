from pandas import IndexSlice as IndexSlice, RangeIndex as RangeIndex
from pandas._config import get_option as get_option
from pandas._typing import Axis as Axis, FilePath as FilePath, IndexLabel as IndexLabel, Level as Level, Scalar as Scalar, WriteBuffer as WriteBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.frame import DataFrame as DataFrame, Series as Series
from pandas.core.generic import NDFrame as NDFrame
from pandas.io.formats.format import save_to_buffer as save_to_buffer
from pandas.io.formats.style_render import CSSProperties as CSSProperties, CSSStyles as CSSStyles, ExtFormatter as ExtFormatter, StylerRenderer as StylerRenderer, Subset as Subset, Tooltips as Tooltips, format_table_styles as format_table_styles, maybe_convert_css_to_tuples as maybe_convert_css_to_tuples, non_reducing_slice as non_reducing_slice, refactor_levels as refactor_levels
from pandas.util._decorators import Substitution as Substitution, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Union, Any, Callable, Hashable, Sequence

jinja2: Any
has_mpl: bool
no_mpl_message: str
subset: str
props: str

class Styler(StylerRenderer):
    precision: Any
    na_rep: Any
    def __init__(self, data: Union[DataFrame, Series], precision: Union[int, None] = ..., table_styles: Union[CSSStyles, None] = ..., uuid: Union[str, None] = ..., caption: Union[str, tuple, None] = ..., table_attributes: Union[str, None] = ..., cell_ids: bool = ..., na_rep: Union[str, None] = ..., uuid_len: int = ..., decimal: Union[str, None] = ..., thousands: Union[str, None] = ..., escape: Union[str, None] = ..., formatter: Union[ExtFormatter, None] = ...) -> None: ...
    def render(self, sparse_index: Union[bool, None] = ..., sparse_columns: Union[bool, None] = ..., **kwargs) -> str: ...
    tooltips: Any
    def set_tooltips(self, ttips: DataFrame, props: Union[CSSProperties, None] = ..., css_class: Union[str, None] = ...) -> Styler: ...
    def to_excel(self, excel_writer, sheet_name: str = ..., na_rep: str = ..., float_format: Union[str, None] = ..., columns: Union[Sequence[Hashable], None] = ..., header: Union[Sequence[Hashable], bool] = ..., index: bool = ..., index_label: Union[IndexLabel, None] = ..., startrow: int = ..., startcol: int = ..., engine: Union[str, None] = ..., merge_cells: bool = ..., encoding: Union[str, None] = ..., inf_rep: str = ..., verbose: bool = ..., freeze_panes: Union[tuple[int, int], None] = ...) -> None: ...
    def to_latex(self, buf: Union[FilePath, WriteBuffer[str], None] = ..., *, column_format: Union[str, None] = ..., position: Union[str, None] = ..., position_float: Union[str, None] = ..., hrules: Union[bool, None] = ..., clines: Union[str, None] = ..., label: Union[str, None] = ..., caption: Union[str, tuple, None] = ..., sparse_index: Union[bool, None] = ..., sparse_columns: Union[bool, None] = ..., multirow_align: Union[str, None] = ..., multicol_align: Union[str, None] = ..., siunitx: bool = ..., environment: Union[str, None] = ..., encoding: Union[str, None] = ..., convert_css: bool = ...): ...
    def to_html(self, buf: Union[FilePath, WriteBuffer[str], None] = ..., *, table_uuid: Union[str, None] = ..., table_attributes: Union[str, None] = ..., sparse_index: Union[bool, None] = ..., sparse_columns: Union[bool, None] = ..., bold_headers: bool = ..., caption: Union[str, None] = ..., max_rows: Union[int, None] = ..., max_columns: Union[int, None] = ..., encoding: Union[str, None] = ..., doctype_html: bool = ..., exclude_styles: bool = ..., **kwargs): ...
    def set_td_classes(self, classes: DataFrame) -> Styler: ...
    def __copy__(self) -> Styler: ...
    def __deepcopy__(self, memo) -> Styler: ...
    def clear(self) -> None: ...
    def apply(self, func: Callable, axis: Union[Axis, None] = ..., subset: Union[Subset, None] = ..., **kwargs) -> Styler: ...
    def apply_index(self, func: Callable, axis: Union[int, str] = ..., level: Union[Level, list[Level], None] = ..., **kwargs) -> Styler: ...
    def applymap_index(self, func: Callable, axis: Union[int, str] = ..., level: Union[Level, list[Level], None] = ..., **kwargs) -> Styler: ...
    def applymap(self, func: Callable, subset: Union[Subset, None] = ..., **kwargs) -> Styler: ...
    def where(self, cond: Callable, value: str, other: Union[str, None] = ..., subset: Union[Subset, None] = ..., **kwargs) -> Styler: ...
    def set_precision(self, precision: int) -> StylerRenderer: ...
    table_attributes: Any
    def set_table_attributes(self, attributes: str) -> Styler: ...
    def export(self) -> dict[str, Any]: ...
    hide_index_names: Any
    hide_column_names: Any
    css: Any
    def use(self, styles: dict[str, Any]) -> Styler: ...
    uuid: Any
    def set_uuid(self, uuid: str) -> Styler: ...
    caption: Any
    def set_caption(self, caption: Union[str, tuple]) -> Styler: ...
    def set_sticky(self, axis: Axis = ..., pixel_size: Union[int, None] = ..., levels: Union[Level, list[Level], None] = ...) -> Styler: ...
    table_styles: Any
    def set_table_styles(self, table_styles: Union[dict[Any, CSSStyles], CSSStyles, None] = ..., axis: int = ..., overwrite: bool = ..., css_class_names: Union[dict[str, str], None] = ...) -> Styler: ...
    def set_na_rep(self, na_rep: str) -> StylerRenderer: ...
    def hide_index(self, subset: Union[Subset, None] = ..., level: Union[Level, list[Level], None] = ..., names: bool = ...) -> Styler: ...
    def hide_columns(self, subset: Union[Subset, None] = ..., level: Union[Level, list[Level], None] = ..., names: bool = ...) -> Styler: ...
    def hide(self, subset: Union[Subset, None] = ..., axis: Axis = ..., level: Union[Level, list[Level], None] = ..., names: bool = ...) -> Styler: ...
    def background_gradient(self, cmap: str = ..., low: float = ..., high: float = ..., axis: Union[Axis, None] = ..., subset: Union[Subset, None] = ..., text_color_threshold: float = ..., vmin: Union[float, None] = ..., vmax: Union[float, None] = ..., gmap: Union[Sequence, None] = ...) -> Styler: ...
    def text_gradient(self, cmap: str = ..., low: float = ..., high: float = ..., axis: Union[Axis, None] = ..., subset: Union[Subset, None] = ..., vmin: Union[float, None] = ..., vmax: Union[float, None] = ..., gmap: Union[Sequence, None] = ...) -> Styler: ...
    def set_properties(self, subset: Union[Subset, None] = ..., **kwargs) -> Styler: ...
    def bar(self, subset: Union[Subset, None] = ..., axis: Union[Axis, None] = ..., *, color: Union[str, list, tuple, None] = ..., cmap: Union[Any, None] = ..., width: float = ..., height: float = ..., align: Union[str, float, int, Callable] = ..., vmin: Union[float, None] = ..., vmax: Union[float, None] = ..., props: str = ...) -> Styler: ...
    def highlight_null(self, null_color: str = ..., subset: Union[Subset, None] = ..., props: Union[str, None] = ...) -> Styler: ...
    def highlight_max(self, subset: Union[Subset, None] = ..., color: str = ..., axis: Union[Axis, None] = ..., props: Union[str, None] = ...) -> Styler: ...
    def highlight_min(self, subset: Union[Subset, None] = ..., color: str = ..., axis: Union[Axis, None] = ..., props: Union[str, None] = ...) -> Styler: ...
    def highlight_between(self, subset: Union[Subset, None] = ..., color: str = ..., axis: Union[Axis, None] = ..., left: Union[Scalar, Sequence, None] = ..., right: Union[Scalar, Sequence, None] = ..., inclusive: str = ..., props: Union[str, None] = ...) -> Styler: ...
    def highlight_quantile(self, subset: Union[Subset, None] = ..., color: str = ..., axis: Union[Axis, None] = ..., q_left: float = ..., q_right: float = ..., interpolation: str = ..., inclusive: str = ..., props: Union[str, None] = ...) -> Styler: ...
    @classmethod
    def from_custom_template(cls, searchpath, html_table: Union[str, None] = ..., html_style: Union[str, None] = ...): ...
    def pipe(self, func: Callable, *args, **kwargs): ...
