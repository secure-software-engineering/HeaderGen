from _typeshed import Incomplete

__all__ = ["netcdf_file", "netcdf_variable"]

class netcdf_file:
    fp: Incomplete
    filename: str
    use_mmap: Incomplete
    mode: Incomplete
    version_byte: Incomplete
    maskandscale: Incomplete
    dimensions: Incomplete
    variables: Incomplete
    def __init__(
        self,
        filename,
        mode: str = "r",
        mmap: Incomplete | None = None,
        version: int = 1,
        maskandscale: bool = False,
    ) -> None: ...
    def __setattr__(self, attr, value) -> None: ...
    def close(self) -> None: ...
    __del__ = close
    def __enter__(self): ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    def createDimension(self, name, length) -> None: ...
    def createVariable(self, name, type, dimensions): ...
    def flush(self) -> None: ...
    sync = flush

class netcdf_variable:
    data: Incomplete
    dimensions: Incomplete
    maskandscale: Incomplete
    def __init__(
        self,
        data,
        typecode,
        size,
        shape,
        dimensions,
        attributes: Incomplete | None = None,
        maskandscale: bool = False,
    ) -> None: ...
    def __setattr__(self, attr, value) -> None: ...
    @property
    def isrec(self): ...
    @property
    def shape(self): ...
    def getValue(self): ...
    def assignValue(self, value) -> None: ...
    def typecode(self): ...
    def itemsize(self): ...
    def __getitem__(self, index): ...
    def __setitem__(self, index, data) -> None: ...

NetCDFFile = netcdf_file
NetCDFVariable = netcdf_variable
