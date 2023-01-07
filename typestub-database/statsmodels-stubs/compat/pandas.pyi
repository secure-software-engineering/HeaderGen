import numpy as np
import pandas as pd
import pandas.util.testing as testing
from pandas._testing import makeDataFrame as make_dataframe
from pandas.core.common import is_numeric_dtype as is_numeric_dtype
from pandas.tseries import frequencies as frequencies
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly, deprecate_kwarg as deprecate_kwarg
from typing import Any, Optional

PD_LT_1_0_0: Any
PD_LT_1_4: Any
data_klasses: Any
assert_frame_equal: Any
assert_index_equal: Any
assert_series_equal: Any

def is_int_index(index: pd.Index) -> bool: ...
def is_float_index(index: pd.Index) -> bool: ...
def to_numpy(po: pd.DataFrame) -> np.ndarray: ...
def get_cached_func(cached_prop): ...
def call_cached_func(cached_prop, *args, **kwargs): ...
def get_cached_doc(cached_prop) -> Optional[str]: ...
