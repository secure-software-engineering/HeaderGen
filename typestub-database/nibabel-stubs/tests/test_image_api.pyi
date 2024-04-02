from collections.abc import Generator

from _typeshed import Incomplete
from nibabel.arraywriters import WriterError as WriterError
from nibabel.testing import assert_data_similar as assert_data_similar
from nibabel.testing import bytesio_filemap as bytesio_filemap
from nibabel.testing import bytesio_round_trip as bytesio_round_trip
from nibabel.testing import clear_and_catch_warnings as clear_and_catch_warnings
from nibabel.testing import deprecated_to as deprecated_to
from nibabel.testing import expires as expires
from nibabel.testing import nullcontext as nullcontext

from .. import AnalyzeImage as AnalyzeImage
from .. import GiftiImage as GiftiImage
from .. import MGHImage as MGHImage
from .. import Minc1Image as Minc1Image
from .. import Minc2Image as Minc2Image
from .. import Nifti1Image as Nifti1Image
from .. import Nifti1Pair as Nifti1Pair
from .. import Nifti2Image as Nifti2Image
from .. import Nifti2Pair as Nifti2Pair
from .. import Spm2AnalyzeImage as Spm2AnalyzeImage
from .. import Spm99AnalyzeImage as Spm99AnalyzeImage
from .. import brikhead as brikhead
from .. import is_proxy as is_proxy
from .. import minc1 as minc1
from .. import minc2 as minc2
from .. import parrec as parrec
from ..casting import sctypes as sctypes
from ..optpkg import optional_package as optional_package
from ..spatialimages import SpatialImage as SpatialImage
from ..tmpdirs import InTemporaryDirectory as InTemporaryDirectory
from .test_api_validators import ValidateAPI as ValidateAPI
from .test_brikhead import EXAMPLE_IMAGES as AFNI_EXAMPLE_IMAGES
from .test_minc1 import EXAMPLE_IMAGES as MINC1_EXAMPLE_IMAGES
from .test_minc2 import EXAMPLE_IMAGES as MINC2_EXAMPLE_IMAGES
from .test_parrec import EXAMPLE_IMAGES as PARREC_EXAMPLE_IMAGES

_: Incomplete
have_scipy: Incomplete
have_h5py: Incomplete

class GenericImageAPI(ValidateAPI):
    has_scaling: bool
    can_save: bool
    standard_extension: str
    def obj_params(self) -> None: ...
    def validate_header(self, imaker, params) -> None: ...
    def validate_filenames(self, imaker, params) -> None: ...
    def validate_no_slicing(self, imaker, params) -> None: ...
    def validate_get_data_deprecated(self, imaker, params) -> None: ...

class GetSetDtypeMixin:
    def validate_dtype(self, imaker, params) -> None: ...

class DataInterfaceMixin(GetSetDtypeMixin):
    meth_names: Incomplete
    def validate_data_interface(self, imaker, params) -> None: ...
    def validate_shape(self, imaker, params) -> None: ...
    def validate_ndim(self, imaker, params) -> None: ...
    def validate_mmap_parameter(self, imaker, params) -> None: ...

class HeaderShapeMixin:
    def validate_header_shape(self, imaker, params) -> None: ...

class AffineMixin:
    def validate_affine(self, imaker, params) -> None: ...

class SerializeMixin:
    def validate_to_from_stream(self, imaker, params) -> None: ...
    def validate_file_stream_equivalence(self, imaker, params) -> None: ...
    def validate_to_from_bytes(self, imaker, params) -> None: ...
    httpserver: Incomplete
    tmp_path: Incomplete
    def setup_method(self, httpserver, tmp_path) -> None: ...
    def validate_from_url(self, imaker, params) -> None: ...
    def validate_from_file_url(self, imaker, params) -> None: ...

class LoadImageAPI(
    GenericImageAPI, DataInterfaceMixin, AffineMixin, GetSetDtypeMixin, HeaderShapeMixin
):
    loader: Incomplete
    example_images: Incomplete
    klass: Incomplete
    def obj_params(self) -> Generator[Incomplete, None, Incomplete]: ...
    def validate_path_maybe_image(self, imaker, params) -> None: ...

class MakeImageAPI(LoadImageAPI):
    image_maker: Incomplete
    header_maker: Incomplete
    example_shapes: Incomplete
    storable_dtypes: Incomplete
    def obj_params(self) -> Generator[Incomplete, None, Incomplete]: ...

class DtypeOverrideMixin(GetSetDtypeMixin):
    def validate_init_dtype_override(self, imaker, params) -> None: ...
    def validate_to_file_dtype_override(self, imaker, params) -> None: ...

class ImageHeaderAPI(MakeImageAPI):
    def header_maker(self): ...

class TestSpatialImageAPI(ImageHeaderAPI):
    klass = SpatialImage
    image_maker = SpatialImage
    can_save: bool

class TestAnalyzeAPI(TestSpatialImageAPI, DtypeOverrideMixin):
    klass = AnalyzeImage
    image_maker = AnalyzeImage
    has_scaling: bool
    can_save: bool
    standard_extension: str
    storable_dtypes: Incomplete

class TestSpm99AnalyzeAPI(TestAnalyzeAPI):
    klass = Spm99AnalyzeImage
    image_maker = Spm99AnalyzeImage
    has_scaling: bool
    can_save = have_scipy

class TestSpm2AnalyzeAPI(TestSpm99AnalyzeAPI):
    klass = Spm2AnalyzeImage
    image_maker = Spm2AnalyzeImage

class TestNifti1PairAPI(TestSpm99AnalyzeAPI):
    klass = Nifti1Pair
    image_maker = Nifti1Pair
    can_save: bool

class TestNifti1API(TestNifti1PairAPI, SerializeMixin):
    klass = Nifti1Image
    image_maker = Nifti1Image
    standard_extension: str

class TestNifti2PairAPI(TestNifti1PairAPI):
    klass = Nifti2Pair
    image_maker = Nifti2Pair

class TestNifti2API(TestNifti1API):
    klass = Nifti2Image
    image_maker = Nifti2Image

class TestMinc1API(ImageHeaderAPI):
    klass = Minc1Image
    image_maker = Minc1Image
    loader: Incomplete
    example_images = MINC1_EXAMPLE_IMAGES

class TestMinc2API(TestMinc1API):
    def setup_method(self) -> None: ...
    klass = Minc2Image
    image_maker = Minc2Image
    loader: Incomplete
    example_images = MINC2_EXAMPLE_IMAGES

class TestPARRECAPI(LoadImageAPI):
    def loader(self, fname): ...
    klass = parrec.PARRECImage
    example_images = PARREC_EXAMPLE_IMAGES

class TestMGHAPI(ImageHeaderAPI, SerializeMixin):
    klass = MGHImage
    image_maker = MGHImage
    example_shapes: Incomplete
    has_scaling: bool
    can_save: bool
    standard_extension: str

class TestGiftiAPI(LoadImageAPI, SerializeMixin):
    klass = GiftiImage
    image_maker = GiftiImage
    can_save: bool
    standard_extension: str

class TestAFNIAPI(LoadImageAPI):
    loader: Incomplete
    klass = brikhead.AFNIImage
    image_maker = brikhead.AFNIImage
    example_images = AFNI_EXAMPLE_IMAGES
