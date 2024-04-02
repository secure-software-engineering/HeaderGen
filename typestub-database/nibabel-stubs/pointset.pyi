import typing as ty
from dataclasses import dataclass

import numpy
from _typeshed import Incomplete
from nibabel.casting import able_int_type as able_int_type
from nibabel.fileslice import strided_scalar as strided_scalar
from nibabel.spatialimages import SpatialImage as SpatialImage
from typing_extensions import Self

class CoordinateArray(ty.Protocol):
    ndim: int
    shape: tuple[int, int]
    @ty.overload
    def __array__(
        self, dtype: None = ...
    ) -> numpyndarray[ty.Any, numpydtype[ty.Any]]: ...
    @ty.overload
    def __array__(self, dtype: _DType) -> numpyndarray[ty.Any, _DType]: ...

@dataclass
class Pointset:
    coordinates: CoordinateArray
    affine: numpyndarray
    homogeneous: bool = ...
    __array_priority__ = ...
    def __init__(
        self,
        coordinates: CoordinateArray,
        affine: numpyndarray | None = None,
        homogeneous: bool = False,
    ) -> None: ...
    @property
    def n_coords(self) -> int: ...
    @property
    def dim(self) -> int: ...
    def __rmatmul__(self, affine: numpyndarray) -> Self: ...
    def get_coords(self, *, as_homogeneous: bool = False): ...

class Grid(Pointset):
    @classmethod
    def from_image(cls, spatialimage: SpatialImage) -> Self: ...
    @classmethod
    def from_mask(cls, mask: SpatialImage) -> Self: ...
    def to_mask(self, shape: Incomplete | None = None) -> SpatialImage: ...

class GridIndices:
    ndim: int
    gridshape: Incomplete
    dtype: Incomplete
    shape: Incomplete
    def __init__(self, shape, dtype: Incomplete | None = None) -> None: ...
    def __array__(self, dtype: Incomplete | None = None): ...
