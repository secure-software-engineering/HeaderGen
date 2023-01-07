import numpy.fft as fftpkg
import numpy.linalg as linpkg
from numpy.lib import i0 as i0

fft = fftpkg.fft
ifft = fftpkg.ifft
fftn = fftpkg.fftn
ifftn = fftpkg.ifftn
fft2 = fftpkg.fft2
ifft2 = fftpkg.ifft2
norm = linpkg.norm
inv = linpkg.inv
svd = linpkg.svd
solve = linpkg.solve
det = linpkg.det
eig = linpkg.eig
eigvals = linpkg.eigvals
eigh = linpkg.eigh
eigvalsh = linpkg.eigvalsh
lstsq = linpkg.lstsq
pinv = linpkg.pinv
cholesky = linpkg.cholesky
