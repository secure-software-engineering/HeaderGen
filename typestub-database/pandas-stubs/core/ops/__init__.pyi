from pandas.core.frame import DataFrame as DataFrame, Series as Series
from pandas._libs.ops_dispatch import maybe_dispatch_ufunc_to_dunder_op as maybe_dispatch_ufunc_to_dunder_op
from pandas._typing import Level as Level
from pandas.core import algorithms as algorithms, roperator as roperator
from pandas.core.dtypes.common import is_array_like as is_array_like, is_list_like as is_list_like
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna
from pandas.core.ops.array_ops import arithmetic_op as arithmetic_op, comp_method_OBJECT_ARRAY as comp_method_OBJECT_ARRAY, comparison_op as comparison_op, get_array_op as get_array_op, logical_op as logical_op, maybe_prepare_scalar_for_op as maybe_prepare_scalar_for_op
from pandas.core.ops.common import get_op_result_name as get_op_result_name, unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.core.ops.docstrings import make_flex_doc as make_flex_doc
from pandas.core.ops.invalid import invalid_comparison as invalid_comparison
from pandas.core.ops.mask_ops import kleene_and as kleene_and, kleene_or as kleene_or, kleene_xor as kleene_xor
from pandas.core.ops.methods import add_flex_arithmetic_methods as add_flex_arithmetic_methods
from pandas.core.roperator import radd as radd, rand_ as rand_, rdiv as rdiv, rdivmod as rdivmod, rfloordiv as rfloordiv, rmod as rmod, rmul as rmul, ror_ as ror_, rpow as rpow, rsub as rsub, rtruediv as rtruediv, rxor as rxor
from pandas.util._decorators import Appender as Appender
from pandas.util._exceptions import find_stack_level as find_stack_level

ARITHMETIC_BINOPS: set[str]
COMPARISON_BINOPS: set[str]

def fill_binop(left, right, fill_value): ...
def align_method_SERIES(left: Series, right, align_asobject: bool = ...): ...
def flex_method_SERIES(op): ...
def align_method_FRAME(left, right, axis, flex: Union[bool, None] = ..., level: Level = ...): ...
def should_reindex_frame_op(left: DataFrame, right, op, axis, default_axis, fill_value, level) -> bool: ...
def frame_arith_method_with_reindex(left: DataFrame, right: DataFrame, op) -> DataFrame: ...
def flex_arith_method_FRAME(op): ...
def flex_comp_method_FRAME(op): ...
