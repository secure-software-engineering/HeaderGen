from _typeshed import Incomplete
from nibabel.cmdline.conform import main as main
from nibabel.optpkg import optional_package as optional_package
from nibabel.testing import get_test_data as get_test_data

_: Incomplete
have_scipy: Incomplete
needs_scipy: Incomplete

def test_default(tmpdir) -> None: ...
def test_nondefault(tmpdir) -> None: ...
