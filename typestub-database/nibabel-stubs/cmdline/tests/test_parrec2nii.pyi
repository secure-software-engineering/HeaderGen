from _typeshed import Incomplete
from nibabel.cmdline import parrec2nii as parrec2nii
from nibabel.tests.test_parrec import EG_PAR as EG_PAR
from nibabel.tests.test_parrec import VARY_PAR as VARY_PAR
from nibabel.tmpdirs import InTemporaryDirectory as InTemporaryDirectory

AN_OLD_AFFINE: Incomplete
PAR_AFFINE: Incomplete

def test_parrec2nii_sets_qform_sform_code1(*args) -> None: ...
def test_parrec2nii_save_load_qform_code(*args) -> None: ...
