from io import StringIO as StringIO

from nibabel import Nifti1Image as Nifti1Image
from nibabel.cmdline.stats import main as main
from nibabel.loadsave import save as save

def test_volume(tmpdir, capsys) -> None: ...
