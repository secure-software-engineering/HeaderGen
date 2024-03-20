import datetime
from typing import (
    IO,
    Any,
    Callable,
    Hashable,
    Iterable,
    Literal,
    Sequence,
    Union,
    overload,
)

import numpy as np
from pandas._config import get_option as get_option
from pandas._libs import lib as lib
from pandas._libs import properties as properties
from pandas._libs.hashtable import duplicated as duplicated
from pandas._libs.lib import no_default as no_default
from pandas._typing import AggFuncType as AggFuncType
from pandas._typing import AnyArrayLike as AnyArrayLike
from pandas._typing import ArrayLike as ArrayLike
from pandas._typing import Axes as Axes
from pandas._typing import Axis as Axis
from pandas._typing import ColspaceArgType as ColspaceArgType
from pandas._typing import CompressionOptions as CompressionOptions
from pandas._typing import Dtype as Dtype
from pandas._typing import DtypeObj as DtypeObj
from pandas._typing import FilePath as FilePath
from pandas._typing import FillnaOptions as FillnaOptions
from pandas._typing import FloatFormatType as FloatFormatType
from pandas._typing import FormattersType as FormattersType
from pandas._typing import Frequency as Frequency
from pandas._typing import IndexKeyFunc as IndexKeyFunc
from pandas._typing import IndexLabel as IndexLabel
from pandas._typing import Level as Level
from pandas._typing import PythonFuncType as PythonFuncType
from pandas._typing import ReadBuffer as ReadBuffer
from pandas._typing import Renamer as Renamer
from pandas._typing import Scalar as Scalar
from pandas._typing import StorageOptions as StorageOptions
from pandas._typing import Suffixes as Suffixes
from pandas._typing import TimedeltaConvertibleTypes as TimedeltaConvertibleTypes
from pandas._typing import TimestampConvertibleTypes as TimestampConvertibleTypes
from pandas._typing import ValueKeyFunc as ValueKeyFunc
from pandas._typing import WriteBuffer as WriteBuffer
from pandas._typing import npt as npt
from pandas.compat._optional import (
    import_optional_dependency as import_optional_dependency,
)
from pandas.core import algorithms as algorithms
from pandas.core import nanops as nanops
from pandas.core import ops as ops
from pandas.core.accessor import CachedAccessor as CachedAccessor
from pandas.core.apply import reconstruct_func as reconstruct_func
from pandas.core.apply import relabel_result as relabel_result
from pandas.core.array_algos.take import take_2d_multi as take_2d_multi
from pandas.core.arraylike import OpsMixin as OpsMixin
from pandas.core.arrays import DatetimeArray as DatetimeArray
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.arrays import TimedeltaArray as TimedeltaArray
from pandas.core.arrays.sparse import SparseFrameAccessor as SparseFrameAccessor
from pandas.core.construction import extract_array as extract_array
from pandas.core.construction import sanitize_array as sanitize_array
from pandas.core.construction import sanitize_masked_array as sanitize_masked_array
from pandas.core.dtypes.cast import can_hold_element as can_hold_element
from pandas.core.dtypes.cast import (
    construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar,
)
from pandas.core.dtypes.cast import (
    construct_2d_arraylike_from_scalar as construct_2d_arraylike_from_scalar,
)
from pandas.core.dtypes.cast import find_common_type as find_common_type
from pandas.core.dtypes.cast import infer_dtype_from_scalar as infer_dtype_from_scalar
from pandas.core.dtypes.cast import invalidate_string_dtypes as invalidate_string_dtypes
from pandas.core.dtypes.cast import maybe_box_native as maybe_box_native
from pandas.core.dtypes.cast import maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int
from pandas.core.dtypes.common import infer_dtype_from_object as infer_dtype_from_object
from pandas.core.dtypes.common import is_1d_only_ea_dtype as is_1d_only_ea_dtype
from pandas.core.dtypes.common import is_1d_only_ea_obj as is_1d_only_ea_obj
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype
from pandas.core.dtypes.common import is_dataclass as is_dataclass
from pandas.core.dtypes.common import is_datetime64_any_dtype as is_datetime64_any_dtype
from pandas.core.dtypes.common import is_dict_like as is_dict_like
from pandas.core.dtypes.common import is_dtype_equal as is_dtype_equal
from pandas.core.dtypes.common import (
    is_extension_array_dtype as is_extension_array_dtype,
)
from pandas.core.dtypes.common import is_float as is_float
from pandas.core.dtypes.common import is_float_dtype as is_float_dtype
from pandas.core.dtypes.common import is_hashable as is_hashable
from pandas.core.dtypes.common import is_integer as is_integer
from pandas.core.dtypes.common import is_integer_dtype as is_integer_dtype
from pandas.core.dtypes.common import is_iterator as is_iterator
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.dtypes.common import is_object_dtype as is_object_dtype
from pandas.core.dtypes.common import is_scalar as is_scalar
from pandas.core.dtypes.common import is_sequence as is_sequence
from pandas.core.dtypes.common import pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.dtypes.missing import notna as notna
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby.generic import DataFrameGroupBy as DataFrameGroupBy
from pandas.core.indexers import check_key_length as check_key_length
from pandas.core.indexes.api import DatetimeIndex as DatetimeIndex
from pandas.core.indexes.api import Index as Index
from pandas.core.indexes.api import PeriodIndex as PeriodIndex
from pandas.core.indexes.api import default_index as default_index
from pandas.core.indexes.api import ensure_index as ensure_index
from pandas.core.indexes.api import (
    ensure_index_from_sequences as ensure_index_from_sequences,
)
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.core.indexes.multi import maybe_droplevels as maybe_droplevels
from pandas.core.indexing import check_bool_indexer as check_bool_indexer
from pandas.core.indexing import check_deprecated_indexers as check_deprecated_indexers
from pandas.core.indexing import (
    convert_to_index_sliceable as convert_to_index_sliceable,
)
from pandas.core.internals import ArrayManager as ArrayManager
from pandas.core.internals import BlockManager as BlockManager
from pandas.core.internals import SingleDataManager as SingleDataManager
from pandas.core.internals.construction import arrays_to_mgr as arrays_to_mgr
from pandas.core.internals.construction import (
    dataclasses_to_dicts as dataclasses_to_dicts,
)
from pandas.core.internals.construction import dict_to_mgr as dict_to_mgr
from pandas.core.internals.construction import mgr_to_mgr as mgr_to_mgr
from pandas.core.internals.construction import ndarray_to_mgr as ndarray_to_mgr
from pandas.core.internals.construction import (
    nested_data_to_arrays as nested_data_to_arrays,
)
from pandas.core.internals.construction import rec_array_to_mgr as rec_array_to_mgr
from pandas.core.internals.construction import reorder_arrays as reorder_arrays
from pandas.core.internals.construction import to_arrays as to_arrays
from pandas.core.internals.construction import treat_as_nested as treat_as_nested
from pandas.core.resample import Resampler as Resampler
from pandas.core.reshape.melt import melt as melt
from pandas.core.series import Series as Series
from pandas.core.sorting import get_group_index as get_group_index
from pandas.core.sorting import lexsort_indexer as lexsort_indexer
from pandas.core.sorting import nargsort as nargsort
from pandas.io.common import get_handle as get_handle
from pandas.io.formats import console as console
from pandas.io.formats import format as fmt
from pandas.io.formats.info import INFO_DOCSTRING as INFO_DOCSTRING
from pandas.io.formats.info import DataFrameInfo as DataFrameInfo
from pandas.io.formats.info import frame_sub_kwargs as frame_sub_kwargs
from pandas.io.formats.style import Styler as Styler
from pandas.util._decorators import Appender as Appender
from pandas.util._decorators import Substitution as Substitution
from pandas.util._decorators import deprecate_kwarg as deprecate_kwarg
from pandas.util._decorators import (
    deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments,
)
from pandas.util._decorators import doc as doc
from pandas.util._decorators import (
    rewrite_axis_style_signature as rewrite_axis_style_signature,
)
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_ascending as validate_ascending
from pandas.util._validators import validate_axis_style_args as validate_axis_style_args
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from pandas.util._validators import validate_percentile as validate_percentile

class DataFrame(NDFrame, OpsMixin):
    def __init__(
        self,
        data: Any | None = ...,
        index: Union[Axes, None] = ...,
        columns: Union[Axes, None] = ...,
        dtype: Union[Dtype, None] = ...,
        copy: Union[bool, None] = ...,
    ) -> None: ...
    @property
    def axes(self) -> list[Index]: ...
    @property
    def shape(self) -> tuple[int, int]: ...
    @overload
    def to_string(
        self,
        buf: None = ...,
        columns: Union[Sequence[str], None] = ...,
        col_space: Union[int, list[int], dict[Hashable, int], None] = ...,
        header: Union[bool, Sequence[str]] = ...,
        index: bool = ...,
        na_rep: str = ...,
        formatters: Union[fmt.FormattersType, None] = ...,
        float_format: Union[fmt.FloatFormatType, None] = ...,
        sparsify: Union[bool, None] = ...,
        index_names: bool = ...,
        justify: Union[str, None] = ...,
        max_rows: Union[int, None] = ...,
        max_cols: Union[int, None] = ...,
        show_dimensions: bool = ...,
        decimal: str = ...,
        line_width: Union[int, None] = ...,
        min_rows: Union[int, None] = ...,
        max_colwidth: Union[int, None] = ...,
        encoding: Union[str, None] = ...,
    ) -> str: ...
    @overload
    def to_string(
        self,
        buf: Union[FilePath, WriteBuffer[str]],
        columns: Union[Sequence[str], None] = ...,
        col_space: Union[int, list[int], dict[Hashable, int], None] = ...,
        header: Union[bool, Sequence[str]] = ...,
        index: bool = ...,
        na_rep: str = ...,
        formatters: Union[fmt.FormattersType, None] = ...,
        float_format: Union[fmt.FloatFormatType, None] = ...,
        sparsify: Union[bool, None] = ...,
        index_names: bool = ...,
        justify: Union[str, None] = ...,
        max_rows: Union[int, None] = ...,
        max_cols: Union[int, None] = ...,
        show_dimensions: bool = ...,
        decimal: str = ...,
        line_width: Union[int, None] = ...,
        min_rows: Union[int, None] = ...,
        max_colwidth: Union[int, None] = ...,
        encoding: Union[str, None] = ...,
    ) -> None: ...
    @property
    def style(self) -> Styler: ...
    def items(self) -> Iterable[tuple[Hashable, Series]]: ...
    def iteritems(self) -> Iterable[tuple[Hashable, Series]]: ...
    def iterrows(self) -> Iterable[tuple[Hashable, Series]]: ...
    def itertuples(
        self, index: bool = ..., name: Union[str, None] = ...
    ) -> Iterable[tuple[Any, ...]]: ...
    def __len__(self) -> int: ...
    @overload
    def dot(self, other: Series) -> Series: ...
    @overload
    def dot(self, other: Union[DataFrame, Index, ArrayLike]) -> DataFrame: ...
    @overload
    def __matmul__(self, other: Series) -> Series: ...
    @overload
    def __matmul__(
        self, other: Union[AnyArrayLike, DataFrame, Series]
    ) -> Union[DataFrame, Series]: ...
    def __rmatmul__(self, other): ...
    @classmethod
    def from_dict(
        cls,
        data,
        orient: str = ...,
        dtype: Union[Dtype, None] = ...,
        columns: Any | None = ...,
    ) -> DataFrame: ...
    def to_numpy(
        self, dtype: Union[npt.DTypeLike, None] = ..., copy: bool = ..., na_value=...
    ) -> np.ndarray: ...
    def to_dict(self, orient: str = ..., into=...): ...
    def to_gbq(
        self,
        destination_table: str,
        project_id: Union[str, None] = ...,
        chunksize: Union[int, None] = ...,
        reauth: bool = ...,
        if_exists: str = ...,
        auth_local_webserver: bool = ...,
        table_schema: Union[list[dict[str, str]], None] = ...,
        location: Union[str, None] = ...,
        progress_bar: bool = ...,
        credentials: Any | None = ...,
    ) -> None: ...
    @classmethod
    def from_records(
        cls,
        data,
        index: Any | None = ...,
        exclude: Any | None = ...,
        columns: Any | None = ...,
        coerce_float: bool = ...,
        nrows: Union[int, None] = ...,
    ) -> DataFrame: ...
    def to_records(
        self,
        index: bool = ...,
        column_dtypes: Any | None = ...,
        index_dtypes: Any | None = ...,
    ) -> np.recarray: ...
    def to_stata(
        self,
        path: Union[FilePath, WriteBuffer[bytes]],
        convert_dates: Union[dict[Hashable, str], None] = ...,
        write_index: bool = ...,
        byteorder: Union[str, None] = ...,
        time_stamp: Union[datetime.datetime, None] = ...,
        data_label: Union[str, None] = ...,
        variable_labels: Union[dict[Hashable, str], None] = ...,
        version: Union[int, None] = ...,
        convert_strl: Union[Sequence[Hashable], None] = ...,
        compression: CompressionOptions = ...,
        storage_options: StorageOptions = ...,
        *,
        value_labels: Union[dict[Hashable, dict[Union[float, int], str]], None] = ...
    ) -> None: ...
    def to_feather(
        self, path: Union[FilePath, WriteBuffer[bytes]], **kwargs
    ) -> None: ...
    def to_markdown(
        self,
        buf: Union[IO[str], str, None] = ...,
        mode: str = ...,
        index: bool = ...,
        storage_options: StorageOptions = ...,
        **kwargs
    ) -> Union[str, None]: ...
    def to_parquet(
        self,
        path: Union[FilePath, WriteBuffer[bytes], None] = ...,
        engine: str = ...,
        compression: Union[str, None] = ...,
        index: Union[bool, None] = ...,
        partition_cols: Union[list[str], None] = ...,
        storage_options: StorageOptions = ...,
        **kwargs
    ) -> Union[bytes, None]: ...
    def to_html(
        self,
        buf: Union[FilePath, WriteBuffer[str], None] = ...,
        columns: Union[Sequence[str], None] = ...,
        col_space: Union[ColspaceArgType, None] = ...,
        header: Union[bool, Sequence[str]] = ...,
        index: bool = ...,
        na_rep: str = ...,
        formatters: Union[FormattersType, None] = ...,
        float_format: Union[FloatFormatType, None] = ...,
        sparsify: Union[bool, None] = ...,
        index_names: bool = ...,
        justify: Union[str, None] = ...,
        max_rows: Union[int, None] = ...,
        max_cols: Union[int, None] = ...,
        show_dimensions: Union[bool, str] = ...,
        decimal: str = ...,
        bold_rows: bool = ...,
        classes: Union[str, list, tuple, None] = ...,
        escape: bool = ...,
        notebook: bool = ...,
        border: Union[int, None] = ...,
        table_id: Union[str, None] = ...,
        render_links: bool = ...,
        encoding: Union[str, None] = ...,
    ): ...
    def to_xml(
        self,
        path_or_buffer: Union[
            FilePath, WriteBuffer[bytes], WriteBuffer[str], None
        ] = ...,
        index: bool = ...,
        root_name: Union[str, None] = ...,
        row_name: Union[str, None] = ...,
        na_rep: Union[str, None] = ...,
        attr_cols: Union[list[str], None] = ...,
        elem_cols: Union[list[str], None] = ...,
        namespaces: Union[dict[Union[str, None], str], None] = ...,
        prefix: Union[str, None] = ...,
        encoding: str = ...,
        xml_declaration: Union[bool, None] = ...,
        pretty_print: Union[bool, None] = ...,
        parser: Union[str, None] = ...,
        stylesheet: Union[FilePath, ReadBuffer[str], ReadBuffer[bytes], None] = ...,
        compression: CompressionOptions = ...,
        storage_options: StorageOptions = ...,
    ) -> Union[str, None]: ...
    def info(
        self,
        verbose: Union[bool, None] = ...,
        buf: Union[WriteBuffer[str], None] = ...,
        max_cols: Union[int, None] = ...,
        memory_usage: Union[bool, str, None] = ...,
        show_counts: Union[bool, None] = ...,
        null_counts: Union[bool, None] = ...,
    ) -> None: ...
    def memory_usage(self, index: bool = ..., deep: bool = ...) -> Series: ...
    def transpose(self, *args, copy: bool = ...) -> DataFrame: ...
    @property
    def T(self) -> DataFrame: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def query(self, expr: str, inplace: bool = ..., **kwargs): ...
    def eval(self, expr: str, inplace: bool = ..., **kwargs): ...
    def select_dtypes(
        self, include: Any | None = ..., exclude: Any | None = ...
    ) -> DataFrame: ...
    def insert(
        self,
        loc: int,
        column: Hashable,
        value: Union[Scalar, AnyArrayLike],
        allow_duplicates: bool = ...,
    ) -> None: ...
    def assign(self, **kwargs) -> DataFrame: ...
    def lookup(
        self, row_labels: Sequence[IndexLabel], col_labels: Sequence[IndexLabel]
    ) -> np.ndarray: ...
    def align(
        self,
        other,
        join: str = ...,
        axis: Union[Axis, None] = ...,
        level: Union[Level, None] = ...,
        copy: bool = ...,
        fill_value: Any | None = ...,
        method: Union[str, None] = ...,
        limit: Any | None = ...,
        fill_axis: Axis = ...,
        broadcast_axis: Union[Axis, None] = ...,
    ) -> DataFrame: ...
    @overload
    def set_axis(
        self, labels, axis: Axis = ..., inplace: Literal[False] = ...
    ) -> DataFrame: ...
    @overload
    def set_axis(self, labels, axis: Axis, inplace: Literal[True]) -> None: ...
    @overload
    def set_axis(self, labels, inplace: Literal[True]) -> None: ...
    @overload
    def set_axis(
        self, labels, axis: Axis = ..., inplace: bool = ...
    ) -> Union[DataFrame, None]: ...
    def reindex(self, *args, **kwargs) -> DataFrame: ...
    def drop(
        self,
        labels: Any | None = ...,
        axis: Axis = ...,
        index: Any | None = ...,
        columns: Any | None = ...,
        level: Union[Level, None] = ...,
        inplace: bool = ...,
        errors: str = ...,
    ) -> DataFrame: ...
    def rename(
        self,
        mapper: Union[Renamer, None] = ...,
        *,
        index: Union[Renamer, None] = ...,
        columns: Union[Renamer, None] = ...,
        axis: Union[Axis, None] = ...,
        copy: bool = ...,
        inplace: bool = ...,
        level: Union[Level, None] = ...,
        errors: str = ...
    ) -> Union[DataFrame, None]: ...
    @overload
    def fillna(
        self,
        value=...,
        method: Union[FillnaOptions, None] = ...,
        axis: Union[Axis, None] = ...,
        inplace: Literal[False] = ...,
        limit=...,
        downcast=...,
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value,
        method: Union[FillnaOptions, None],
        axis: Union[Axis, None],
        inplace: Literal[True],
        limit=...,
        downcast=...,
    ) -> None: ...
    @overload
    def fillna(self, inplace: Literal[True], *, limit=..., downcast=...) -> None: ...
    @overload
    def fillna(
        self, value, inplace: Literal[True], *, limit=..., downcast=...
    ) -> None: ...
    @overload
    def fillna(
        self,
        method: Union[FillnaOptions, None],
        inplace: Literal[True],
        *,
        limit=...,
        downcast=...
    ) -> None: ...
    @overload
    def fillna(
        self,
        axis: Union[Axis, None],
        inplace: Literal[True],
        *,
        limit=...,
        downcast=...
    ) -> None: ...
    @overload
    def fillna(
        self,
        method: Union[FillnaOptions, None],
        axis: Union[Axis, None],
        inplace: Literal[True],
        *,
        limit=...,
        downcast=...
    ) -> None: ...
    @overload
    def fillna(
        self,
        value,
        axis: Union[Axis, None],
        inplace: Literal[True],
        *,
        limit=...,
        downcast=...
    ) -> None: ...
    @overload
    def fillna(
        self,
        value,
        method: Union[FillnaOptions, None],
        inplace: Literal[True],
        *,
        limit=...,
        downcast=...
    ) -> None: ...
    @overload
    def fillna(
        self,
        value=...,
        method: Union[FillnaOptions, None] = ...,
        axis: Union[Axis, None] = ...,
        inplace: bool = ...,
        limit=...,
        downcast=...,
    ) -> Union[DataFrame, None]: ...
    def pop(self, item: Hashable) -> Series: ...
    def replace(
        self,
        to_replace: Any | None = ...,
        value=...,
        inplace: bool = ...,
        limit: Any | None = ...,
        regex: bool = ...,
        method: Union[str, lib.NoDefault] = ...,
    ) -> DataFrame: ...
    def shift(
        self,
        periods: int = ...,
        freq: Union[Frequency, None] = ...,
        axis: Axis = ...,
        fill_value=...,
    ) -> DataFrame: ...
    def set_index(
        self,
        keys,
        drop: bool = ...,
        append: bool = ...,
        inplace: bool = ...,
        verify_integrity: bool = ...,
    ) -> DataFrame: ...
    @overload
    def reset_index(
        self,
        level: Union[Hashable, Sequence[Hashable], None] = ...,
        drop: bool = ...,
        inplace: Literal[False] = ...,
        col_level: Hashable = ...,
        col_fill: Hashable = ...,
    ) -> DataFrame: ...
    @overload
    def reset_index(
        self,
        level: Union[Hashable, Sequence[Hashable], None],
        drop: bool,
        inplace: Literal[True],
        col_level: Hashable = ...,
        col_fill: Hashable = ...,
    ) -> None: ...
    @overload
    def reset_index(
        self,
        drop: bool,
        inplace: Literal[True],
        *,
        col_level: Hashable = ...,
        col_fill: Hashable = ...
    ) -> None: ...
    @overload
    def reset_index(
        self,
        level: Union[Hashable, Sequence[Hashable], None],
        inplace: Literal[True],
        *,
        col_level: Hashable = ...,
        col_fill: Hashable = ...
    ) -> None: ...
    @overload
    def reset_index(
        self,
        inplace: Literal[True],
        *,
        col_level: Hashable = ...,
        col_fill: Hashable = ...
    ) -> None: ...
    @overload
    def reset_index(
        self,
        level: Union[Hashable, Sequence[Hashable], None] = ...,
        drop: bool = ...,
        inplace: bool = ...,
        col_level: Hashable = ...,
        col_fill: Hashable = ...,
    ) -> Union[DataFrame, None]: ...
    def isna(self) -> DataFrame: ...
    def isnull(self) -> DataFrame: ...
    def notna(self) -> DataFrame: ...
    def notnull(self) -> DataFrame: ...
    def dropna(
        self,
        axis: Axis = ...,
        how: str = ...,
        thresh: Any | None = ...,
        subset: IndexLabel = ...,
        inplace: bool = ...,
    ) -> DataFrame: ...
    def drop_duplicates(
        self,
        subset: Union[Hashable, Sequence[Hashable], None] = ...,
        keep: Union[Literal[first], Literal[last], Literal[False]] = ...,
        inplace: bool = ...,
        ignore_index: bool = ...,
    ) -> Union[DataFrame, None]: ...
    def duplicated(
        self,
        subset: Union[Hashable, Sequence[Hashable], None] = ...,
        keep: Union[Literal[first], Literal[last], Literal[False]] = ...,
    ) -> Series: ...
    def sort_values(
        self,
        by,
        axis: Axis = ...,
        ascending: bool = ...,
        inplace: bool = ...,
        kind: str = ...,
        na_position: str = ...,
        ignore_index: bool = ...,
        key: ValueKeyFunc = ...,
    ) -> DataFrame: ...
    def sort_index(
        self,
        axis: Axis = ...,
        level: Union[Level, None] = ...,
        ascending: Union[bool, int, Sequence[Union[bool, int]]] = ...,
        inplace: bool = ...,
        kind: str = ...,
        na_position: str = ...,
        sort_remaining: bool = ...,
        ignore_index: bool = ...,
        key: IndexKeyFunc = ...,
    ) -> DataFrame: ...
    def value_counts(
        self,
        subset: Union[Sequence[Hashable], None] = ...,
        normalize: bool = ...,
        sort: bool = ...,
        ascending: bool = ...,
        dropna: bool = ...,
    ) -> Series: ...
    def nlargest(self, n: int, columns: IndexLabel, keep: str = ...) -> DataFrame: ...
    def nsmallest(self, n: int, columns: IndexLabel, keep: str = ...) -> DataFrame: ...
    def swaplevel(
        self, i: Axis = ..., j: Axis = ..., axis: Axis = ...
    ) -> DataFrame: ...
    def reorder_levels(self, order: Sequence[Axis], axis: Axis = ...) -> DataFrame: ...
    def __divmod__(self, other) -> tuple[DataFrame, DataFrame]: ...
    def __rdivmod__(self, other) -> tuple[DataFrame, DataFrame]: ...
    def compare(
        self,
        other: DataFrame,
        align_axis: Axis = ...,
        keep_shape: bool = ...,
        keep_equal: bool = ...,
    ) -> DataFrame: ...
    def combine(
        self,
        other: DataFrame,
        func,
        fill_value: Any | None = ...,
        overwrite: bool = ...,
    ) -> DataFrame: ...
    def combine_first(self, other: DataFrame) -> DataFrame: ...
    def update(
        self,
        other,
        join: str = ...,
        overwrite: bool = ...,
        filter_func: Any | None = ...,
        errors: str = ...,
    ) -> None: ...
    def groupby(
        self,
        by: Any | None = ...,
        axis: Axis = ...,
        level: Union[Level, None] = ...,
        as_index: bool = ...,
        sort: bool = ...,
        group_keys: bool = ...,
        squeeze: Union[bool, lib.NoDefault] = ...,
        observed: bool = ...,
        dropna: bool = ...,
    ) -> DataFrameGroupBy: ...
    def pivot(
        self,
        index: Any | None = ...,
        columns: Any | None = ...,
        values: Any | None = ...,
    ) -> DataFrame: ...
    def pivot_table(
        self,
        values: Any | None = ...,
        index: Any | None = ...,
        columns: Any | None = ...,
        aggfunc: str = ...,
        fill_value: Any | None = ...,
        margins: bool = ...,
        dropna: bool = ...,
        margins_name: str = ...,
        observed: bool = ...,
        sort: bool = ...,
    ) -> DataFrame: ...
    def stack(self, level: Level = ..., dropna: bool = ...): ...
    def explode(self, column: IndexLabel, ignore_index: bool = ...) -> DataFrame: ...
    def unstack(self, level: Level = ..., fill_value: Any | None = ...): ...
    def melt(
        self,
        id_vars: Any | None = ...,
        value_vars: Any | None = ...,
        var_name: Any | None = ...,
        value_name: str = ...,
        col_level: Union[Level, None] = ...,
        ignore_index: bool = ...,
    ) -> DataFrame: ...
    def diff(self, periods: int = ..., axis: Axis = ...) -> DataFrame: ...
    def aggregate(
        self, func: Any | None = ..., axis: Axis = ..., *args, **kwargs
    ) -> Union[DataFrame, Series]: ...
    agg: Any
    def transform(
        self, func: AggFuncType, axis: Axis = ..., *args, **kwargs
    ) -> DataFrame: ...
    def apply(
        self,
        func: AggFuncType,
        axis: Axis = ...,
        raw: bool = ...,
        result_type: Any | None = ...,
        args=...,
        **kwargs
    ): ...
    def applymap(
        self, func: PythonFuncType, na_action: Union[str, None] = ..., **kwargs
    ) -> DataFrame: ...
    def append(
        self,
        other,
        ignore_index: bool = ...,
        verify_integrity: bool = ...,
        sort: bool = ...,
    ) -> DataFrame: ...
    def join(
        self,
        other: Union[DataFrame, Series],
        on: Union[IndexLabel, None] = ...,
        how: str = ...,
        lsuffix: str = ...,
        rsuffix: str = ...,
        sort: bool = ...,
    ) -> DataFrame: ...
    def merge(
        self,
        right: Union[DataFrame, Series],
        how: str = ...,
        on: Union[IndexLabel, None] = ...,
        left_on: Union[IndexLabel, None] = ...,
        right_on: Union[IndexLabel, None] = ...,
        left_index: bool = ...,
        right_index: bool = ...,
        sort: bool = ...,
        suffixes: Suffixes = ...,
        copy: bool = ...,
        indicator: bool = ...,
        validate: Union[str, None] = ...,
    ) -> DataFrame: ...
    def round(
        self, decimals: Union[int, dict[IndexLabel, int], Series] = ..., *args, **kwargs
    ) -> DataFrame: ...
    def corr(
        self,
        method: Union[str, Callable[[np.ndarray, np.ndarray], float]] = ...,
        min_periods: int = ...,
    ) -> DataFrame: ...
    def cov(
        self, min_periods: Union[int, None] = ..., ddof: Union[int, None] = ...
    ) -> DataFrame: ...
    def corrwith(
        self, other, axis: Axis = ..., drop: bool = ..., method: str = ...
    ) -> Series: ...
    def count(
        self,
        axis: Axis = ...,
        level: Union[Level, None] = ...,
        numeric_only: bool = ...,
    ): ...
    def nunique(self, axis: Axis = ..., dropna: bool = ...) -> Series: ...
    def idxmin(self, axis: Axis = ..., skipna: bool = ...) -> Series: ...
    def idxmax(self, axis: Axis = ..., skipna: bool = ...) -> Series: ...
    def mode(
        self, axis: Axis = ..., numeric_only: bool = ..., dropna: bool = ...
    ) -> DataFrame: ...
    def quantile(
        self,
        q: float = ...,
        axis: Axis = ...,
        numeric_only: bool = ...,
        interpolation: str = ...,
    ): ...
    def asfreq(
        self,
        freq: Frequency,
        method: Any | None = ...,
        how: Union[str, None] = ...,
        normalize: bool = ...,
        fill_value: Any | None = ...,
    ) -> DataFrame: ...
    def resample(
        self,
        rule,
        axis: int = ...,
        closed: Union[str, None] = ...,
        label: Union[str, None] = ...,
        convention: str = ...,
        kind: Union[str, None] = ...,
        loffset: Any | None = ...,
        base: Union[int, None] = ...,
        on: Any | None = ...,
        level: Any | None = ...,
        origin: Union[str, TimestampConvertibleTypes] = ...,
        offset: Union[TimedeltaConvertibleTypes, None] = ...,
    ) -> Resampler: ...
    def to_timestamp(
        self,
        freq: Union[Frequency, None] = ...,
        how: str = ...,
        axis: Axis = ...,
        copy: bool = ...,
    ) -> DataFrame: ...
    def to_period(
        self, freq: Union[Frequency, None] = ..., axis: Axis = ..., copy: bool = ...
    ) -> DataFrame: ...
    def isin(self, values) -> DataFrame: ...
    index: Index
    columns: Index
    plot: Any
    hist: Any
    boxplot: Any
    sparse: Any
    @property
    def values(self) -> np.ndarray: ...
    def ffill(
        self,
        axis: Union[None, Axis] = ...,
        inplace: bool = ...,
        limit: Union[None, int] = ...,
        downcast: Any | None = ...,
    ) -> Union[DataFrame, None]: ...
    def bfill(
        self,
        axis: Union[None, Axis] = ...,
        inplace: bool = ...,
        limit: Union[None, int] = ...,
        downcast: Any | None = ...,
    ) -> Union[DataFrame, None]: ...
    def clip(
        self,
        lower: Any | None = ...,
        upper: Any | None = ...,
        axis: Union[Axis, None] = ...,
        inplace: bool = ...,
        *args,
        **kwargs
    ) -> Union[DataFrame, None]: ...
    def interpolate(
        self,
        method: str = ...,
        axis: Axis = ...,
        limit: Union[int, None] = ...,
        inplace: bool = ...,
        limit_direction: Union[str, None] = ...,
        limit_area: Union[str, None] = ...,
        downcast: Union[str, None] = ...,
        **kwargs
    ) -> Union[DataFrame, None]: ...
    def where(
        self,
        cond,
        other=...,
        inplace: bool = ...,
        axis: Any | None = ...,
        level: Any | None = ...,
        errors: str = ...,
        try_cast=...,
    ): ...
    def mask(
        self,
        cond,
        other=...,
        inplace: bool = ...,
        axis: Any | None = ...,
        level: Any | None = ...,
        errors: str = ...,
        try_cast=...,
    ): ...
