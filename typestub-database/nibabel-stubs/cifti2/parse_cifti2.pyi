from _typeshed import Incomplete

from .. import xmlutils as xml
from ..batteryrunners import Report as Report
from ..nifti1 import Nifti1Extension as Nifti1Extension
from ..nifti1 import extension_codes as extension_codes
from ..nifti1 import intent_codes as intent_codes
from ..nifti2 import Nifti2Header as Nifti2Header
from ..nifti2 import Nifti2Image as Nifti2Image
from ..spatialimages import HeaderDataError as HeaderDataError
from .cifti2 import CIFTI_BRAIN_STRUCTURES as CIFTI_BRAIN_STRUCTURES
from .cifti2 import CIFTI_MODEL_TYPES as CIFTI_MODEL_TYPES
from .cifti2 import Cifti2BrainModel as Cifti2BrainModel
from .cifti2 import Cifti2Header as Cifti2Header
from .cifti2 import Cifti2HeaderError as Cifti2HeaderError
from .cifti2 import Cifti2Label as Cifti2Label
from .cifti2 import Cifti2LabelTable as Cifti2LabelTable
from .cifti2 import Cifti2Matrix as Cifti2Matrix
from .cifti2 import Cifti2MatrixIndicesMap as Cifti2MatrixIndicesMap
from .cifti2 import Cifti2MetaData as Cifti2MetaData
from .cifti2 import Cifti2NamedMap as Cifti2NamedMap
from .cifti2 import Cifti2Parcel as Cifti2Parcel
from .cifti2 import Cifti2Surface as Cifti2Surface
from .cifti2 import (
    Cifti2TransformationMatrixVoxelIndicesIJKtoXYZ as Cifti2TransformationMatrixVoxelIndicesIJKtoXYZ,
)
from .cifti2 import Cifti2VertexIndices as Cifti2VertexIndices
from .cifti2 import Cifti2Vertices as Cifti2Vertices
from .cifti2 import Cifti2Volume as Cifti2Volume
from .cifti2 import Cifti2VoxelIndicesIJK as Cifti2VoxelIndicesIJK

class Cifti2Extension(Nifti1Extension):
    code: int
    def __init__(
        self, code: Incomplete | None = None, content: Incomplete | None = None
    ) -> None: ...

class _Cifti2AsNiftiHeader(Nifti2Header):
    @classmethod
    def may_contain_header(klass, binaryblock): ...

class _Cifti2AsNiftiImage(Nifti2Image):
    header_class: Incomplete
    makeable: bool

class Cifti2Parser(xml.XmlParser):
    fsm_state: Incomplete
    struct_state: Incomplete
    write_to: Incomplete
    header: Incomplete
    def __init__(
        self,
        encoding: Incomplete | None = None,
        buffer_size: int = 3500000,
        verbose: int = 0,
    ) -> None: ...
    def StartElementHandler(self, name, attrs) -> None: ...
    def EndElementHandler(self, name) -> None: ...
    def CharacterDataHandler(self, data) -> None: ...
    def flush_chardata(self) -> None: ...
    @property
    def pending_data(self): ...
