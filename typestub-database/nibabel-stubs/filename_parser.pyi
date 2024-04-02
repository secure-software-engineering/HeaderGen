import typing as ty

from _typeshed import Incomplete

FileSpec: Incomplete
ExtensionSpec: Incomplete

class TypesFilenamesError(Exception): ...

def types_filenames(
    template_fname: FileSpec,
    types_exts: ty.Sequence[ExtensionSpec],
    trailing_suffixes: ty.Sequence[str] = (".gz", ".bz2"),
    enforce_extensions: bool = True,
    match_case: bool = False,
) -> dict[str, str]: ...
def parse_filename(
    filename: FileSpec,
    types_exts: ty.Sequence[ExtensionSpec],
    trailing_suffixes: ty.Sequence[str],
    match_case: bool = False,
) -> tuple[str, str, str | None, str | None]: ...
def splitext_addext(
    filename: FileSpec,
    addexts: ty.Sequence[str] = (".gz", ".bz2", ".zst"),
    match_case: bool = False,
) -> tuple[str, str, str]: ...
