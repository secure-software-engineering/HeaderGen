from sklearn.compose import make_column_transformer as make_column_transformer
from sklearn.datasets import load_breast_cancer as load_breast_cancer, load_iris as load_iris
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.linear_model import LogisticRegression as LogisticRegression
from sklearn.metrics import auc as auc, plot_roc_curve as plot_roc_curve, roc_curve as roc_curve
from sklearn.model_selection import train_test_split as train_test_split
from sklearn.pipeline import make_pipeline as make_pipeline
from sklearn.preprocessing import StandardScaler as StandardScaler
from sklearn.utils import shuffle as shuffle
from typing import Any

pytestmark: Any

def data(): ...
def data_binary(data): ...
def test_plot_roc_curve(pyplot, response_method, data_binary, with_sample_weight, drop_intermediate, with_strings) -> None: ...
def test_roc_curve_not_fitted_errors(pyplot, data_binary, clf) -> None: ...
def test_plot_roc_curve_pos_label(pyplot, response_method) -> None: ...
