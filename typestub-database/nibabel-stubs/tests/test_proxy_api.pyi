from collections.abc import Generator

from _typeshed import Incomplete

from .. import ecat as ecat
from .. import minc1 as minc1
from .. import minc2 as minc2
from .. import parrec as parrec
from ..analyze import AnalyzeHeader as AnalyzeHeader
from ..arrayproxy import ArrayProxy as ArrayProxy
from ..arrayproxy import is_proxy as is_proxy
from ..casting import have_binary128 as have_binary128
from ..casting import sctypes as sctypes
from ..externals.netcdf import netcdf_file as netcdf_file
from ..freesurfer.mghformat import MGHHeader as MGHHeader
from ..nifti1 import Nifti1Header as Nifti1Header
from ..optpkg import optional_package as optional_package
from ..spm2analyze import Spm2AnalyzeHeader as Spm2AnalyzeHeader
from ..spm99analyze import Spm99AnalyzeHeader as Spm99AnalyzeHeader
from ..testing import assert_dt_equal as assert_dt_equal
from ..testing import clear_and_catch_warnings as clear_and_catch_warnings
from ..tmpdirs import InTemporaryDirectory as InTemporaryDirectory
from ..volumeutils import apply_read_scaling as apply_read_scaling
from .test_api_validators import ValidateAPI as ValidateAPI
from .test_parrec import EG_REC as EG_REC
from .test_parrec import VARY_REC as VARY_REC

h5py: Incomplete
have_h5py: Incomplete
_: Incomplete

class _TestProxyAPI(ValidateAPI):
    settable_offset: bool
    def validate_shape(self, pmaker, params) -> None: ...
    def validate_ndim(self, pmaker, params) -> None: ...
    def validate_is_proxy(self, pmaker, params) -> None: ...
    def validate_asarray(self, pmaker, params) -> None: ...
    def validate_array_interface_with_dtype(self, pmaker, params) -> None: ...
    def validate_header_isolated(self, pmaker, params) -> None: ...
    def validate_fileobj_isolated(self, pmaker, params) -> None: ...
    def validate_proxy_slicing(self, pmaker, params) -> None: ...

class TestAnalyzeProxyAPI(_TestProxyAPI):
    proxy_class = ArrayProxy
    header_class = AnalyzeHeader
    shapes: Incomplete
    has_slope: bool
    has_inter: bool
    data_dtypes: Incomplete
    array_order: str
    settable_offset: bool
    data_endian: str
    def obj_params(self) -> Generator[Incomplete, None, Incomplete]: ...
    def validate_dtype(self, pmaker, params) -> None: ...
    def validate_slope_inter_offset(self, pmaker, params) -> None: ...

class TestSpm99AnalyzeProxyAPI(TestAnalyzeProxyAPI):
    header_class = Spm99AnalyzeHeader
    has_slope: bool

class TestSpm2AnalyzeProxyAPI(TestSpm99AnalyzeProxyAPI):
    header_class = Spm2AnalyzeHeader

class TestNifti1ProxyAPI(TestSpm99AnalyzeProxyAPI):
    header_class = Nifti1Header
    has_inter: bool
    data_dtypes: Incomplete

class TestMGHAPI(TestAnalyzeProxyAPI):
    header_class = MGHHeader
    shapes: Incomplete
    has_slope: bool
    has_inter: bool
    settable_offset: bool
    data_endian: str
    data_dtypes: Incomplete

class TestMinc1API(_TestProxyAPI):
    module = minc1
    file_class = minc1.Minc1File
    eg_fname: str
    eg_shape: Incomplete
    @staticmethod
    def opener(f): ...
    def obj_params(self) -> Generator[Incomplete, None, Incomplete]: ...

class TestMinc2API(TestMinc1API):
    module = minc2
    file_class = minc2.Minc2File
    eg_fname: str
    eg_shape: Incomplete
    @staticmethod
    def opener(f): ...

class TestEcatAPI(_TestProxyAPI):
    eg_fname: str
    eg_shape: Incomplete
    def obj_params(self) -> Generator[Incomplete, None, Incomplete]: ...
    def validate_header_isolated(self, pmaker, params) -> None: ...

class TestPARRECAPI(_TestProxyAPI):
    def obj_params(self) -> Generator[Incomplete, None, None]: ...
