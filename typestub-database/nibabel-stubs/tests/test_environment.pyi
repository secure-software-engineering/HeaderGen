from collections.abc import Generator

DATA_KEY: str
USER_KEY: str

def with_environment(request) -> Generator[None, None, None]: ...
def test_nipy_home() -> None: ...
def test_user_dir(with_environment) -> None: ...
def test_sys_dir() -> None: ...
