from nibabel.affines import apply_affine as apply_affine
from nibabel.affines import from_matvec as from_matvec
from nibabel.affines import to_matvec as to_matvec
from nibabel.filename_parser import splitext_addext as splitext_addext
from nibabel.mriutils import MRIError as MRIError
from nibabel.mriutils import calculate_dwell_time as calculate_dwell_time
from nibabel.orientations import apply_orientation as apply_orientation
from nibabel.orientations import inv_ornt_aff as inv_ornt_aff
from nibabel.orientations import io_orientation as io_orientation
from nibabel.parrec import one_line as one_line
from nibabel.volumeutils import fname_ext_ul_case as fname_ext_ul_case

def get_opt_parser(): ...
def verbose(msg, indent: int = 0) -> None: ...
def error(msg, exit_code) -> None: ...
def proc_file(infile, opts) -> None: ...
def main() -> None: ...
