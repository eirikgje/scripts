#Script to experiment with gaussian beam

from __future__ import division

import numpy as np
import healpix as heal

def gaussbeam_al0(l):
    return np.sqrt((2*l+1)/(4*np.pi))*np.exp(-l*(l+1)*sigma*sigma/2)

nside = 16
npix = 12*nside*nside
lmax = 2*nside
pixsize = np.sqrt(4*np.pi/npix)

beam_alm = np.zeros((1, lmax+1, lmax+1), dtype=complex)
beam_pix = np.zeros(npix)

ell = np.arange(0, lmax+1)
FWHM = 2*pixsize
sigma = FWHM/(2*np.sqrt(2*np.log(2)))

print lmax

beam_alm[0,:,0] = gaussbeam_al0(ell)

print beam_alm[0,:,0]
heal.lib.alm2map_sc_d(nside, lmax, lmax, beam_alm, beam_pix)

heal.lib.convert_ring2nest_d(nside, beam_pix[:, None])

heal.utils.map2gif(beam_pix, 'beamtest.gif')
