from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

chainnum = 1
l = 10
lmax = 90
nsamps = 850

samps = np.zeros((nsamps, 2*lmax-2, 7))

for sampnum in range(nsamps):
    prefix = '/mn/svati/u1/eirikgje/data/commander/chains_titan/easysim/'
    samps[sampnum] = np.loadtxt(prefix + 'cl_c%(chain)04d_k%(samp)05d.dat'%{'chain':chainnum, 'samp':sampnum+1})

x = np.arange(1,nsamps+1)
plt.plot(x, samps[:, l-2, 1])
plt.figure()
plt.plot(x, samps[:, l-2, 2])
plt.figure()
plt.plot(x, samps[:, l-2, 4])
