from io import BytesIO as BytesIO

from nibabel.volumeutils import array_to_file as array_to_file

from .butils import print_git_title as print_git_title

def bench_array_to_file() -> None: ...
