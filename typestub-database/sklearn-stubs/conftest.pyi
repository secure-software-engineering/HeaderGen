from sklearn._min_dependencies import PYTEST_MIN_VERSION as PYTEST_MIN_VERSION
from sklearn.datasets import fetch_20newsgroups as fetch_20newsgroups, fetch_20newsgroups_vectorized as fetch_20newsgroups_vectorized, fetch_california_housing as fetch_california_housing, fetch_covtype as fetch_covtype, fetch_kddcup99 as fetch_kddcup99, fetch_olivetti_faces as fetch_olivetti_faces, fetch_rcv1 as fetch_rcv1
from sklearn.utils.fixes import np_version as np_version, parse_version as parse_version
from typing import Any

dataset_fetchers: Any
fetch_20newsgroups_fxt: Any
fetch_20newsgroups_vectorized_fxt: Any
fetch_california_housing_fxt: Any
fetch_covtype_fxt: Any
fetch_kddcup99_fxt: Any
fetch_olivetti_faces_fxt: Any
fetch_rcv1_fxt: Any

def pytest_collection_modifyitems(config, items) -> None: ...
def pyplot() -> None: ...
def pytest_runtest_setup(item) -> None: ...
def pytest_configure(config) -> None: ...
