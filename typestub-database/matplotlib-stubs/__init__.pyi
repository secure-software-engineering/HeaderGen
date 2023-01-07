from collections.abc import MutableMapping
from matplotlib.cbook import MatplotlibDeprecationWarning as MatplotlibDeprecationWarning, mplDeprecation as mplDeprecation, sanitize_sequence as sanitize_sequence
from matplotlib.rcsetup import cycler as cycler, validate_backend as validate_backend
from typing import Any, NamedTuple

__bibtex__: str

class __getattr__:
    __version_info__: Any
    URL_REGEX: Any

def set_loglevel(level) -> None: ...

class _ExecInfo(NamedTuple):
    executable: Any
    version: Any

class ExecutableNotFoundError(FileNotFoundError): ...

def checkdep_usetex(s): ...
def get_configdir(): ...
def get_cachedir(): ...
def get_data_path(): ...
def matplotlib_fname(): ...

def rc_params(fail_on_error: bool = ...): ...
def is_url(filename): ...
def rc_params_from_file(fname, fail_on_error: bool = ..., use_default_template: bool = ...): ...

rcParamsDefault: Any
rcParams: Any
rcParamsOrig: Any
defaultParams: Any

def rc(group, **kwargs) -> None: ...
def rcdefaults() -> None: ...
def rc_file_defaults() -> None: ...
def rc_file(fname, *, use_default_template: bool = ...) -> None: ...
def rc_context(rc: Any | None = ..., fname: Any | None = ...) -> None: ...
def use(backend, *, force: bool = ...) -> None: ...
def get_backend(): ...
def interactive(b) -> None: ...
def is_interactive(): ...

default_test_modules: Any

def test(verbosity: Any | None = ..., coverage: bool = ..., **kwargs): ...
