from unittest import TestCase

from _typeshed import Incomplete

from ..ecat import EcatHeader as EcatHeader
from ..ecat import EcatImage as EcatImage
from ..ecat import EcatSubHeader as EcatSubHeader
from ..ecat import get_frame_order as get_frame_order
from ..ecat import get_series_framenumbers as get_series_framenumbers
from ..ecat import read_mlist as read_mlist
from ..openers import Opener as Opener
from ..testing import data_path as data_path
from ..testing import suppress_warnings as suppress_warnings
from ..tmpdirs import InTemporaryDirectory as InTemporaryDirectory
from . import test_wrapstruct as tws
from .test_fileslice import slicer_samples as slicer_samples

ecat_file: Incomplete

class TestEcatHeader(tws._TestWrapStructBase):
    header_class = EcatHeader
    example_file = ecat_file
    def test_header_size(self) -> None: ...
    def test_empty(self) -> None: ...
    def test_dtype(self) -> None: ...
    def test_header_codes(self) -> None: ...
    def test_update(self) -> None: ...
    def test_from_eg_file(self) -> None: ...

class TestEcatMlist(TestCase):
    header_class = EcatHeader
    example_file = ecat_file
    def test_mlist(self) -> None: ...
    def test_mlist_errors(self) -> None: ...

class TestEcatSubHeader(TestCase):
    header_class = EcatHeader
    subhdr_class = EcatSubHeader
    example_file = ecat_file
    fid: Incomplete
    hdr: Incomplete
    mlist: Incomplete
    subhdr: Incomplete
    def test_subheader_size(self) -> None: ...
    def test_subheader(self) -> None: ...

class TestEcatImage(TestCase):
    image_class = EcatImage
    example_file = ecat_file
    img: Incomplete
    def test_file(self) -> None: ...
    def test_save(self) -> None: ...
    def test_data(self) -> None: ...
    def test_array_proxy(self) -> None: ...
    def test_array_proxy_slicing(self) -> None: ...
    def test_isolation(self) -> None: ...
    def test_float_affine(self) -> None: ...
    def test_data_regression(self) -> None: ...
    def test_mlist_regression(self) -> None: ...
