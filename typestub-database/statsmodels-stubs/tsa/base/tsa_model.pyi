import statsmodels.base.model as base
import statsmodels.base.wrapper as wrap
from statsmodels.base.data import PandasData as PandasData
from statsmodels.compat.pandas import is_float_index as is_float_index, is_int_index as is_int_index, is_numeric_dtype as is_numeric_dtype
from statsmodels.tools.sm_exceptions import ValueWarning as ValueWarning
from typing import Any

def get_index_loc(key, index): ...
def get_index_label_loc(key, index, row_labels): ...
def get_prediction_index(start, end, nobs, base_index, index: Any | None = ..., silent: bool = ..., index_none: bool = ..., index_generated: Any | None = ..., data: Any | None = ...): ...

class TimeSeriesModel(base.LikelihoodModel):
    __doc__: Any
    def __init__(self, endog, exog: Any | None = ..., dates: Any | None = ..., freq: Any | None = ..., missing: str = ..., **kwargs) -> None: ...
    exog_names: Any

class TimeSeriesModelResults(base.LikelihoodModelResults):
    data: Any
    def __init__(self, model, params, normalized_cov_params, scale: float = ...) -> None: ...

class TimeSeriesResultsWrapper(wrap.ResultsWrapper): ...
