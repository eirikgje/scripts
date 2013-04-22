#Script to simulate a simple map with uncorrelated noise and beam values
from __future__ import division

import healpix as heal
import numpy as np

nside = 32
FWHM = 5/180*np.pi
rms_TT = 1
rms_qu = 1
npix = 12*nside**2
lmax = 95
sigma = FWHM/(2*np.sqrt(2*np.log(2)))

map = np.zeros((npix, 3))
alm = np.zeros((3, lmax+1, lmax+1), dtype=complex)
cls = np.loadtxt('testcls.dat')
newcls = cls[0:lmax-1, :]
normcls = newcls
chol = np.zeros((3, 3, lmax-1))
beam = np.zeros(lmax-1)

for l in range(2,lmax+1):
    beam[l-2] = np.sqrt((2*l+1)/(4*np.pi))*np.exp(-l*(l+1)*sigma*sigma/2)
    normcls[l-2, 1:] = newcls[l-2, 1:]*2*np.pi/(l*(l+1))

chol[0, 0, :] = np.sqrt(normcls[:, 1])
chol[1, 0, :] = normcls[:, 4]/chol[0, 0, :]
chol[1, 1, :] = np.sqrt(normcls[:, 2]-chol[1, 0, :]*chol[1, 0, :])
chol[2, 0, :] = 0
chol[2, 1, :] = 0
chol[2, 2, :] = np.sqrt(normcls[:, 3]-chol[2, 0, :]*chol[2, 0, :]-chol[2, 1, :]*chol[2, 1, :])

x = np.zeros((3, 2))

np.random.seed(41)
for l in range(2, lmax+1):
    for m in range(l+1):
        for i in range(2):
            eta = np.random.randn(3)
            x[0, i] = chol[0, 0, l-2]*eta[0]
            x[1, i] = chol[1, 0, l-2]*eta[0] + chol[1, 1, l-2]*eta[1]
            x[2, i] = chol[2, 0, l-2]*eta[0] + chol[2, 1, l-2]*eta[1] + chol[2, 2, l-2]*eta[2]
        if m == 0:
            for i in range(3):
                alm[i, l, m] = np.complex(x[i, 0], 0)
        else:
            for i in range(3):
                alm[i, l, m] = np.complex(x[i, 0], x[i, 1])
    alm[:, l, :] = alm[:, l, :]*beam[l-2] 

for i in range(3):
    tempalm = alm[i, :, :]
    heal.alm2map_sc_d(nside, lmax, lmax, tempalm.reshape((1, lmax+1, lmax+1)), map[:, i])

#Adding noise
#noise = np.zeros((npix, 3))
#rms = np.zeros((npix, 3))
#rms[:, 0] = 1.0
#rms[:, 1:2] = 0.1
#for i in range(3):
#    noise[:, i] = rms[:, i]*np.random.randn(npix)
#map = map + noise

heal.lib.convert_ring2nest_d(nside, map)
heal.nestedmap_to_fits(map[:, 0], 'simmap_T.fits', map_units='muK')
heal.nestedmap_to_fits(map[:, 1], 'simmap_Q.fits', map_units='muK')
heal.nestedmap_to_fits(map[:, 2], 'simmap_U.fits', map_units='muK')
#heal.utils.map2gif(map[:, 0], 'simmap_TT.gif')
#heal.utils.map2gif(map[:, 1], 'simmap_EE.gif')
#heal.utils.map2gif(map[:, 2], 'simmap_BB.gif')
