from _typeshed import Incomplete

from .. import Nifti1Header as Nifti1Header
from .. import Nifti1Image as Nifti1Image
from ..arraywriters import ScalingError as ScalingError
from ..casting import best_float as best_float
from ..casting import sctypes as sctypes
from ..casting import type_info as type_info
from ..casting import ulp as ulp
from ..spatialimages import HeaderDataError as HeaderDataError
from ..spatialimages import supported_np_types as supported_np_types

DEBUG: bool

def round_trip(arr, out_dtype): ...
def check_params(in_arr, in_type, out_type): ...

BFT: Incomplete
LOGe2: Incomplete

def big_bad_ulp(arr): ...
def test_big_bad_ulp() -> None: ...

BIG_FLOAT: Incomplete

def test_round_trip() -> None: ...
def check_arr(test_id, V_in, in_type, out_type, scaling_type) -> None: ...
