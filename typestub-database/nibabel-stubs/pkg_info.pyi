from ._version import __version__ as __version__

COMMIT_HASH: str

def cmp_pkg_version(version_str: str, pkg_version_str: str = ...) -> int: ...
def pkg_commit_hash(pkg_path: str | None = None) -> tuple[str, str]: ...
def get_pkg_info(pkg_path: str) -> dict[str, str]: ...