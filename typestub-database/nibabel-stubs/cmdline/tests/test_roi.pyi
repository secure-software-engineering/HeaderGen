from nibabel.cmdline.roi import lossless_slice as lossless_slice
from nibabel.cmdline.roi import main as main
from nibabel.cmdline.roi import parse_slice as parse_slice
from nibabel.testing import data_path as data_path

def test_parse_slice() -> None: ...
def test_parse_slice_disallow_step() -> None: ...
def test_lossless_slice_unknown_axes() -> None: ...
def test_lossless_slice_scaling(tmp_path) -> None: ...
def test_lossless_slice_noscaling(tmp_path) -> None: ...
def test_nib_roi(tmp_path, inplace) -> None: ...
def test_nib_roi_bad_slices(capsys, args, errmsg) -> None: ...
def test_entrypoint(capsys) -> None: ...
def test_nib_roi_unknown_axes(capsys) -> None: ...
