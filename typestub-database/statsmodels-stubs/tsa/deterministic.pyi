import abc
import numpy as np
import pandas as pd
from abc import ABC, abstractmethod
from statsmodels.compat.pandas import Appender as Appender, is_int_index as is_int_index, to_numpy as to_numpy
from statsmodels.iolib.summary import d_or_f as d_or_f
from statsmodels.tools.validation import bool_like as bool_like, float_like as float_like, required_int_like as required_int_like, string_like as string_like
from statsmodels.tsa.tsatools import freq_to_period as freq_to_period
from typing import Any, Hashable, List, Optional, Sequence, Union

DateLike: Any
IntLike = Union[int, np.integer]
START_BEFORE_INDEX_ERR: str

class DeterministicTerm(ABC, metaclass=abc.ABCMeta):
    @property
    def is_dummy(self) -> bool: ...
    @abstractmethod
    def in_sample(self, index: Sequence[Hashable]) -> pd.DataFrame: ...
    @abstractmethod
    def out_of_sample(self, steps: int, index: Sequence[Hashable], forecast_index: Optional[Sequence[Hashable]] = ...) -> pd.DataFrame: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...

class TimeTrendDeterministicTerm(DeterministicTerm, ABC, metaclass=abc.ABCMeta):
    def __init__(self, constant: bool = ..., order: int = ...) -> None: ...
    @property
    def constant(self) -> bool: ...
    @property
    def order(self) -> int: ...

class TimeTrend(TimeTrendDeterministicTerm):
    def __init__(self, constant: bool = ..., order: int = ...) -> None: ...
    @classmethod
    def from_string(cls, trend: str) -> TimeTrend: ...
    def in_sample(self, index: Union[Sequence[Hashable], pd.Index]) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Union[Sequence[Hashable], pd.Index], forecast_index: Optional[Sequence[Hashable]] = ...) -> pd.DataFrame: ...

class Seasonality(DeterministicTerm):
    def __init__(self, period: int, initial_period: int = ...) -> None: ...
    @property
    def period(self) -> int: ...
    @property
    def initial_period(self) -> int: ...
    @classmethod
    def from_index(cls, index: Union[Sequence[Hashable], pd.DatetimeIndex, pd.PeriodIndex]) -> Seasonality: ...
    def in_sample(self, index: Union[Sequence[Hashable], pd.Index]) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Union[Sequence[Hashable], pd.Index], forecast_index: Optional[Sequence[Hashable]] = ...) -> pd.DataFrame: ...

class FourierDeterministicTerm(DeterministicTerm, ABC, metaclass=abc.ABCMeta):
    def __init__(self, order: int) -> None: ...
    @property
    def order(self) -> int: ...

class Fourier(FourierDeterministicTerm):
    def __init__(self, period: float, order: int) -> None: ...
    @property
    def period(self) -> float: ...
    def in_sample(self, index: Union[Sequence[Hashable], pd.Index]) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Union[Sequence[Hashable], pd.Index], forecast_index: Optional[Sequence[Hashable]] = ...) -> pd.DataFrame: ...

class CalendarDeterministicTerm(DeterministicTerm, ABC, metaclass=abc.ABCMeta):
    def __init__(self, freq: str) -> None: ...
    @property
    def freq(self) -> str: ...

class CalendarFourier(CalendarDeterministicTerm, FourierDeterministicTerm):
    def __init__(self, freq: str, order: int) -> None: ...
    def in_sample(self, index: Union[Sequence[Hashable], pd.Index]) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Union[Sequence[Hashable], pd.Index], forecast_index: Optional[Sequence[Hashable]] = ...) -> pd.DataFrame: ...

class CalendarSeasonality(CalendarDeterministicTerm):
    def __init__(self, freq: str, period: str) -> None: ...
    @property
    def freq(self) -> str: ...
    @property
    def period(self) -> str: ...
    def in_sample(self, index: Union[Sequence[Hashable], pd.Index]) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Union[Sequence[Hashable], pd.Index], forecast_index: Optional[Sequence[Hashable]] = ...) -> pd.DataFrame: ...

class CalendarTimeTrend(CalendarDeterministicTerm, TimeTrendDeterministicTerm):
    def __init__(self, freq: str, constant: bool = ..., order: int = ..., *, base_period: Optional[Union[str, DateLike]] = ...) -> None: ...
    @property
    def base_period(self) -> Optional[str]: ...
    @classmethod
    def from_string(cls, freq: str, trend: str, base_period: Optional[Union[str, DateLike]] = ...) -> CalendarTimeTrend: ...
    def in_sample(self, index: Union[Sequence[Hashable], pd.Index]) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, index: Union[Sequence[Hashable], pd.Index], forecast_index: Optional[Sequence[Hashable]] = ...) -> pd.DataFrame: ...

class DeterministicProcess:
    def __init__(self, index: Union[Sequence[Hashable], pd.Index], *, period: Optional[Union[float, int]] = ..., constant: bool = ..., order: int = ..., seasonal: bool = ..., fourier: int = ..., additional_terms: Sequence[DeterministicTerm] = ..., drop: bool = ...) -> None: ...
    @property
    def index(self) -> pd.Index: ...
    @property
    def terms(self) -> List[DeterministicTerm]: ...
    def in_sample(self) -> pd.DataFrame: ...
    def out_of_sample(self, steps: int, forecast_index: Optional[Union[Sequence[Hashable], pd.Index]] = ...) -> pd.DataFrame: ...
    def range(self, start: Union[IntLike, DateLike, str], stop: Union[IntLike, DateLike, str]) -> pd.DataFrame: ...
