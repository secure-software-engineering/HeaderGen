from numpy.distutils import log as log
from numpy.distutils.ccompiler import replace_method as replace_method
from typing import Any

def UnixCCompiler__compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts) -> None: ...
def UnixCCompiler_create_static_lib(self, objects, output_libname, output_dir: Any | None = ..., debug: int = ..., target_lang: Any | None = ...) -> None: ...
