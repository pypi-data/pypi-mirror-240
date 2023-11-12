from functools import partial
from typing import List

import numpy as np
import scipy.constants as cn
import scipy.fft


POISSON_SLICES = {
    'periodic': slice(0, -1),
    'dirichlet': slice(1, -1),
    'neumann': slice(0, None),
}

POISSON_FFT_FORWARDS = {
    'periodic': scipy.fft.fft,
    'dirichlet': partial(scipy.fft.dst, type=1),
    'neumann': partial(scipy.fft.dct, type=1),
}

POISSON_FFT_BACKWARDS = {
    'periodic': scipy.fft.ifft,
    'dirichlet': partial(scipy.fft.idst, type=1),
    'neumann': partial(scipy.fft.idct, type=1),
}


def __calc_modified_wave_number(k, n, boundary_type):
    if (boundary_type == 'periodic'):
        if (k <= int(n/2)):
            wn = 2.0*np.sin(np.pi*k/float(n))
        else:
            wn = 2.0*np.sin(np.pi*(n - k)/float(n))
        wn = -wn*wn

    elif(boundary_type == 'dirichlet'):
        wn = 2.0*(np.cos(np.pi*(k + 1)/float(n + 1)) - 1.0)

    elif(boundary_type == 'neumann'):
        wn = 2.0*(np.cos(np.pi*(k)/float(n)) - 1.0)

    return wn


def poisson(rho: np.ndarray,
            boundary_types: List[str] = ['periodic', 'periodic', 'periodic'],
            btypes: str = None,
            dx: float = 1.0,
            epsilon_0=cn.epsilon_0):
    """Solve Poisson's equation with FFT.

    Parameters
    ----------
    rho : np.ndarray
        3-dimentional array of the charge density [C/m^3]. The shape is (nz+1, ny+1, nx+1).
    boundary_types : List[str] of {'periodic', 'dirichlet', 'neumann'},
        the boundary condition types,
        by default ['periodic', 'periodic', 'periodic'].
    btypes : str
        string consisting of prefixes of boundary conditions, by default None.
        If this is set, it takes precedence over boundary_types.
    dx : float, optional
        the grid width [m], by default 1.0
    epsilon_0 : _type_, optional
        the electric constant (vacuum permittivity) [F/m], by default cn.epsilon_0

    Returns
    -------
    np.ndarray
        3-dimentional of the potential [V].

    """
    # If a boundary condition is specified in abbreviated form, revert to the original notation.
    if btypes:
        btypes_dict = {
            'p': 'periodic',
            'd': 'dirichlet',
            'n': 'neumann',
        }
        boundary_types = [btypes_dict[btype] for btype in btypes]

    # Poisson's equation: dphi/dx^2 = -rho/epsilon_0
    rho = -rho / epsilon_0 * dx*dx

    slices = [POISSON_SLICES[_type] for _type in boundary_types]
    forward = [POISSON_FFT_FORWARDS[_type] for _type in boundary_types]
    backward = [POISSON_FFT_BACKWARDS[_type] for _type in boundary_types]

    # FFT forward.
    rhok = rho[slices[2], slices[1], slices[0]]
    rhok = forward[2](rhok, axis=0, norm='ortho')
    rhok = forward[1](rhok, axis=1, norm='ortho')
    rhok = forward[0](rhok, axis=2, norm='ortho')

    # Caluculate a modified wave number.
    modified_wave_number = np.zeros_like(rhok, dtype=float)
    nz, ny, nx = np.array(rho.shape)-1
    for kx in range(rhok.shape[2]):
        modified_wave_number[:, :, kx] \
            += __calc_modified_wave_number(kx, nx, boundary_types[0])
    for ky in range(rhok.shape[1]):
        modified_wave_number[:, ky, :] \
            += __calc_modified_wave_number(ky, ny, boundary_types[1])
    for kz in range(rhok.shape[0]):
        modified_wave_number[kz, :, :] \
            += __calc_modified_wave_number(kz, nz, boundary_types[2])

    # Solve the equation in the wavenumber domain
    phik = rhok/modified_wave_number

    # When all boundary conditions are periodic boundaries, there is no reference for the potential
    # and it is not uniquely determined, so the average is set to zero
    if all([_type == 'periodic' for _type in boundary_types]):
        phik[0, 0, 0] = 0.

    # FFT backward
    _phi = phik
    _phi = backward[2](_phi, axis=0, norm='ortho')
    _phi = backward[1](_phi, axis=1, norm='ortho')
    _phi = backward[0](_phi, axis=2, norm='ortho')

    # Create an array of the same shape as the input rho array.
    phi = np.zeros_like(rho)
    phi[slices[2], slices[1], slices[0]] = _phi

    # Copy the value of an axis that is a periodic boundary.
    if boundary_types[0] == 'periodic':
        phi[:, :, -1] = phi[:, :, 0]
    if boundary_types[1] == 'periodic':
        phi[:, -1, :] = phi[:, 0, :]
    if boundary_types[2] == 'periodic':
        phi[-1, :, :] = phi[0, :, :]

    return phi
