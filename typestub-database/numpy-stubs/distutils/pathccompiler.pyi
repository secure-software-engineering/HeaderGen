from distutils.unixccompiler import UnixCCompiler

class PathScaleCCompiler(UnixCCompiler):
    compiler_type: str
    cc_exe: str
    cxx_exe: str
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...
