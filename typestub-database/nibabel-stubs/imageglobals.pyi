from _typeshed import Incomplete

error_level: int
logger: Incomplete

class ErrorLevel:
    level: Incomplete
    def __init__(self, level) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc: type[BaseException] | None,
        value: BaseException | None,
        tb: types.TracebackType | None,
    ): ...

class LoggingOutputSuppressor:
    orig_handlers: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc: type[BaseException] | None,
        value: BaseException | None,
        tb: types.TracebackType | None,
    ) -> None: ...
