import numpy as np
from pandas import Index as Index
from pandas._typing import ArrayLike as ArrayLike, T as T, npt as npt
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray
from pandas.core.internals.blocks import Block as B
from typing import Union, Iterator, Sequence, overload

def slice_len(slc: slice, objlen: int = ...) -> int: ...
def get_blkno_indexers(blknos: np.ndarray, group: bool = ...) -> list[tuple[int, Union[slice, np.ndarray]]]: ...
def get_blkno_placements(blknos: np.ndarray, group: bool = ...) -> Iterator[tuple[int, BlockPlacement]]: ...
def update_blklocs_and_blknos(blklocs: npt.NDArray[np.intp], blknos: npt.NDArray[np.intp], loc: int, nblocks: int) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]: ...

class BlockPlacement:
    def __init__(self, val: Union[int, slice, np.ndarray]) -> None: ...
    @property
    def indexer(self) -> Union[np.ndarray, slice]: ...
    @property
    def as_array(self) -> np.ndarray: ...
    @property
    def as_slice(self) -> slice: ...
    @property
    def is_slice_like(self) -> bool: ...
    @overload
    def __getitem__(self, loc: Union[slice, Sequence[int]]) -> BlockPlacement: ...
    @overload
    def __getitem__(self, loc: int) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...
    def delete(self, loc) -> BlockPlacement: ...
    def append(self, others: list[BlockPlacement]) -> BlockPlacement: ...
    def tile_for_unstack(self, factor: int) -> npt.NDArray[np.intp]: ...

class SharedBlock:
    ndim: int
    values: ArrayLike
    def __init__(self, values: ArrayLike, placement: BlockPlacement, ndim: int) -> None: ...

class NumpyBlock(SharedBlock):
    values: np.ndarray
    def getitem_block_index(self, slicer: slice) -> T: ...

class NDArrayBackedBlock(SharedBlock):
    values: NDArrayBackedExtensionArray
    def getitem_block_index(self, slicer: slice) -> T: ...

class Block(SharedBlock): ...

class BlockManager:
    blocks: tuple[B, ...]
    axes: list[Index]
    def __init__(self, blocks: tuple[B, ...], axes: list[Index], verify_integrity=...) -> None: ...
    def get_slice(self, slobj: slice, axis: int = ...) -> T: ...
