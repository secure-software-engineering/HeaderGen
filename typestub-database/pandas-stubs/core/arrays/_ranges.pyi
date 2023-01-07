from pandas._libs.lib import i8max as i8max
from pandas._libs.tslibs import BaseOffset as BaseOffset, OutOfBoundsDatetime as OutOfBoundsDatetime, Timedelta as Timedelta, Timestamp as Timestamp, iNaT as iNaT

def generate_regular_range(start: Union[Timestamp, Timedelta], end: Union[Timestamp, Timedelta], periods: int, freq: BaseOffset): ...
