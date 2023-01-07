from statsmodels.compat.python import lrange as lrange, lzip as lzip
from typing import Any

def combine_indices(groups, prefix: str = ..., sep: str = ..., return_labels: bool = ...): ...
def group_sums(x, group, use_bincount: bool = ...): ...
def group_sums_dummy(x, group_dummy): ...
def dummy_sparse(groups): ...

class Group:
    name: Any
    n_groups: Any
    separator: str
    prefix: Any
    def __init__(self, group, name: str = ...) -> None: ...
    def counts(self): ...
    def labels(self): ...
    def dummy(self, drop_idx: Any | None = ..., sparse: bool = ..., dtype=...): ...
    def interaction(self, other): ...
    def group_sums(self, x, use_bincount: bool = ...): ...
    def group_demean(self, x, use_bincount: bool = ...): ...

class GroupSorted(Group):
    groupidx: Any
    def __init__(self, group, name: str = ...) -> None: ...
    def group_iter(self) -> None: ...
    def lag_indices(self, lag): ...

class Grouping:
    index: Any
    nobs: Any
    nlevels: Any
    slices: Any
    def __init__(self, index, names: Any | None = ...) -> None: ...
    @property
    def index_shape(self): ...
    @property
    def levels(self): ...
    @property
    def labels(self): ...
    @property
    def group_names(self): ...
    def reindex(self, index: Any | None = ..., names: Any | None = ...) -> None: ...
    def get_slices(self, level: int = ...) -> None: ...
    counts: Any
    def count_categories(self, level: int = ...) -> None: ...
    def check_index(self, is_sorted: bool = ..., unique: bool = ..., index: Any | None = ...) -> None: ...
    def sort(self, data, index: Any | None = ...): ...
    def transform_dataframe(self, dataframe, function, level: int = ..., **kwargs): ...
    def transform_array(self, array, function, level: int = ..., **kwargs): ...
    def transform_slices(self, array, function, level: int = ..., **kwargs): ...
    def dummies_time(self): ...
    def dummies_groups(self, level: int = ...): ...
    def dummy_sparse(self, level: int = ...) -> None: ...
