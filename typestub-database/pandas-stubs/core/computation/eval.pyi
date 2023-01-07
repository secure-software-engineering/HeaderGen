from pandas._libs.lib import no_default as no_default
from pandas.core.computation.engines import ENGINES as ENGINES
from pandas.core.computation.expr import Expr as Expr, PARSERS as PARSERS
from pandas.core.computation.ops import BinOp as BinOp
from pandas.core.computation.parsing import tokenize_string as tokenize_string
from pandas.core.computation.scope import ensure_scope as ensure_scope
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Union, Any

def eval(expr: Union[str, BinOp], parser: str = ..., engine: Union[str, None] = ..., truediv=..., local_dict: Any | None = ..., global_dict: Any | None = ..., resolvers=..., level: int = ..., target: Any | None = ..., inplace: bool = ...): ...
