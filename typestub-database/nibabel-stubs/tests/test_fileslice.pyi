from collections.abc import Generator

from _typeshed import Incomplete

from ..fileslice import calc_slicedefs as calc_slicedefs
from ..fileslice import canonical_slicers as canonical_slicers
from ..fileslice import fileslice as fileslice
from ..fileslice import fill_slicer as fill_slicer
from ..fileslice import is_fancy as is_fancy
from ..fileslice import optimize_read_slicers as optimize_read_slicers
from ..fileslice import optimize_slicer as optimize_slicer
from ..fileslice import predict_shape as predict_shape
from ..fileslice import read_segments as read_segments
from ..fileslice import slice2len as slice2len
from ..fileslice import slice2outax as slice2outax
from ..fileslice import slicers2segments as slicers2segments
from ..fileslice import strided_scalar as strided_scalar
from ..fileslice import threshold_heuristic as threshold_heuristic

def test_is_fancy() -> None: ...
def test_canonical_slicers() -> None: ...
def test_slice2outax() -> None: ...
def test_slice2len() -> None: ...
def test_fill_slicer() -> None: ...
def test__positive_slice() -> None: ...
def test_threshold_heuristic() -> None: ...
def test_optimize_slicer() -> None: ...
def test_optimize_read_slicers() -> None: ...
def test_slicers2segments() -> None: ...
def test_calc_slicedefs() -> None: ...
def test_predict_shape() -> None: ...
def test_strided_scalar() -> None: ...
def test_read_segments() -> None: ...
def test_read_segments_lock(): ...
def slicer_samples(shape) -> Generator[Incomplete, Incomplete, None]: ...
def test_fileslice() -> None: ...
def test_fileslice_dtype() -> None: ...
def test_fileslice_errors() -> None: ...
def test_fileslice_heuristic() -> None: ...
