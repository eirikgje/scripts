from __future__ import division
import numpy as np
from matplotlib import pyplot as plt

l = 10 
prefix = '/mn/svati/u1/eirikgje/data/commander/histdata/titan/easysim/'

#if l < 10:
#    filename1 = prefix + 'clsamps_.dat'.format(l)
#    filename2 = prefix + 'sigsamps_000{0}.dat'.format(l)
#elif l < 100:
#    filename1 = prefix + 'clsamps_00{0}.dat'.format(l)
#    filename2 = prefix + 'sigsamps_00{0}.dat'.format(l)
#elif l < 1000:
#    filename1 = prefix + 'clsamps_0{0}.dat'.format(l)
#    filename2 = prefix + 'sigsamps_0{0}.dat'.format(l)

filename1 = prefix + 'clsamps_%(ell)04d.dat'%{'ell':l}
filename2 = prefix + 'sigsamps_%(ell)04d.dat'%{'ell':l}
clsamps = np.loadtxt(filename1)
sigsamps = np.loadtxt(filename2)

plt.clf()
plt.hist(sigsamps[:, 0], histtype='step', bins=50)
plt.hist(clsamps[:, 0], histtype='step', bins=50)
plt.figure()
plt.clf()
plt.hist(sigsamps[:, 1], histtype='step', bins=50)
plt.hist(clsamps[:, 1], histtype='step', bins=50)
plt.figure()
plt.clf()
plt.hist(sigsamps[:, 2], histtype='step', bins=50)
plt.hist(clsamps[:, 2], histtype='step', bins=50)
