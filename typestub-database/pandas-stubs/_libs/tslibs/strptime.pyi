import numpy as np
from pandas._typing import npt as npt

def array_strptime(values: npt.NDArray[np.object_], fmt: Union[str, None], exact: bool = ..., errors: str = ...) -> tuple[np.ndarray, np.ndarray]: ...
