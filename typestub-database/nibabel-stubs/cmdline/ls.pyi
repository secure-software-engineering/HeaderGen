from _typeshed import Incomplete
from nibabel.cmdline.utils import ap as ap
from nibabel.cmdline.utils import safe_get as safe_get
from nibabel.cmdline.utils import table2string as table2string
from nibabel.cmdline.utils import verbose as verbose

MAX_UNIQUE: int

def get_opt_parser(): ...
def proc_file(f, opts): ...
def main(args: Incomplete | None = None) -> None: ...
