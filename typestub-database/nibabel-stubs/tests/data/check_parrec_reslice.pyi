from _typeshed import Incomplete
from nibabel import parrec as parrec
from nibabel.affines import to_matvec as to_matvec
from nibabel.optpkg import optional_package as optional_package

_: Incomplete
have_scipy: Incomplete

def resample_img2img(img_to, img_from, order: int = 1, out_class=...): ...
def gmean_norm(data): ...
