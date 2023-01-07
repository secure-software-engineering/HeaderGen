from .openmp_helpers import check_openmp_support as check_openmp_support
from .pre_build_helpers import basic_check_build as basic_check_build

DEFAULT_ROOT: str

def cythonize_extensions(top_path, config) -> None: ...
def gen_from_templates(templates) -> None: ...
