from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

chainnum = 1
l = 70
lmax = 90

samps = np.zeros((1000, 2*lmax-2, 7))
for sampnum in range(1, 1001):
    prefix = '/mn/svati/u1/eirikgje/data/commander/chains_titan/easysim/'
    samps[sampnum-1] = np.loadtxt(prefix + 'cl_c%(chain)04d_k%(samp)05d.dat'%{'chain':chainnum, 'samp':sampnum})

plt.hist(samps[:, l-2, 1], histtype='step', bins=40)
plt.hist(samps[:, lmax + l-3, 1], histtype='step', bins=40)
