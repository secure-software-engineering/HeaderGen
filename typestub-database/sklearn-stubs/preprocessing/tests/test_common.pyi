from sklearn.base import clone as clone
from sklearn.datasets import load_iris as load_iris
from sklearn.model_selection import train_test_split as train_test_split
from sklearn.preprocessing import MaxAbsScaler as MaxAbsScaler, MinMaxScaler as MinMaxScaler, PowerTransformer as PowerTransformer, QuantileTransformer as QuantileTransformer, RobustScaler as RobustScaler, StandardScaler as StandardScaler, maxabs_scale as maxabs_scale, minmax_scale as minmax_scale, power_transform as power_transform, quantile_transform as quantile_transform, robust_scale as robust_scale, scale as scale
from sklearn.utils._testing import assert_allclose as assert_allclose, assert_array_equal as assert_array_equal
from typing import Any

iris: Any

def test_missing_value_handling(est, func, support_sparse, strictly_positive, omit_kwargs) -> None: ...
def test_missing_value_pandas_na_support(est, func) -> None: ...
