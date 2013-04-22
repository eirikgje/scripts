from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

chainnum = 1
lmax = 90
numsamps = 350

for sampnum in range(numsamps):
    prefix = '/mn/svati/u1/eirikgje/data/commander/chains_titan/easysim/'
    cl = np.loadtxt(prefix + 'cl_c%(chain)04d_k%(samp)05d.dat'%{'chain':chainnum, 'samp':sampnum+1})

    plt.figure(1)
    plt.plot(cl[0:lmax-1, 0], cl[0:lmax-1, 1])
    plt.figure(2)
    plt.plot(cl[lmax-1:2*lmax-2, 0], cl[lmax-1:2*lmax-2, 1])
    plt.figure(3)
    plt.plot(cl[0:lmax-1, 0], cl[0:lmax-1, 2])
    plt.figure(4)
    plt.plot(cl[lmax-1:2*lmax-2, 0], cl[lmax-1:2*lmax-2, 2])
    plt.figure(5)
    plt.plot(cl[0:lmax-1, 0], cl[0:lmax-1, 4])
    plt.figure(6)
    plt.plot(cl[lmax-1:2*lmax-2, 0], cl[lmax-1:2*lmax-2, 4])

