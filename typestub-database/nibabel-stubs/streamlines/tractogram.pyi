import abc
from collections.abc import MutableMapping

from _typeshed import Incomplete
from nibabel.affines import apply_affine as apply_affine

from .array_sequence import ArraySequence as ArraySequence

def is_data_dict(obj): ...
def is_lazy_dict(obj): ...

class SliceableDataDict(MutableMapping, metaclass=abc.ABCMeta):
    store: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __contains__(self, key) -> bool: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class PerArrayDict(SliceableDataDict):
    n_rows: Incomplete
    def __init__(self, n_rows: int = 0, *args, **kwargs) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def extend(self, other) -> None: ...

class PerArraySequenceDict(PerArrayDict):
    def __setitem__(self, key, value) -> None: ...

class LazyDict(MutableMapping):
    store: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class TractogramItem:
    streamline: Incomplete
    data_for_streamline: Incomplete
    data_for_points: Incomplete
    def __init__(self, streamline, data_for_streamline, data_for_points) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class Tractogram:
    def __init__(
        self,
        streamlines: Incomplete | None = None,
        data_per_streamline: Incomplete | None = None,
        data_per_point: Incomplete | None = None,
        affine_to_rasmm: Incomplete | None = None,
    ) -> None: ...
    @property
    def streamlines(self): ...
    @property
    def data_per_streamline(self): ...
    @data_per_streamline.setter
    def data_per_streamline(self, value) -> None: ...
    @property
    def data_per_point(self): ...
    @data_per_point.setter
    def data_per_point(self, value) -> None: ...
    @property
    def affine_to_rasmm(self): ...
    @affine_to_rasmm.setter
    def affine_to_rasmm(self, value) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
    def copy(self): ...
    def apply_affine(self, affine, lazy: bool = False): ...
    def to_world(self, lazy: bool = False): ...
    def extend(self, other) -> None: ...
    def __iadd__(self, other): ...
    def __add__(self, other): ...

class LazyTractogram(Tractogram):
    def __init__(
        self,
        streamlines: Incomplete | None = None,
        data_per_streamline: Incomplete | None = None,
        data_per_point: Incomplete | None = None,
        affine_to_rasmm: Incomplete | None = None,
    ) -> None: ...
    @classmethod
    def from_tractogram(cls, tractogram): ...
    @classmethod
    def from_data_func(cls, data_func): ...
    @property
    def streamlines(self): ...
    @property
    def data_per_streamline(self): ...
    @data_per_streamline.setter
    def data_per_streamline(self, value) -> None: ...
    @property
    def data_per_point(self): ...
    @data_per_point.setter
    def data_per_point(self, value) -> None: ...
    @property
    def data(self): ...
    def __getitem__(self, idx) -> None: ...
    def extend(self, other) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def copy(self): ...
    def apply_affine(self, affine, lazy: bool = True): ...
    def to_world(self, lazy: bool = True): ...
