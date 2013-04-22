from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

chainnum = 1
l = 10
lmax = 90
nsamps = 850
prefix = '/mn/svati/u1/eirikgje/data/commander/chains_titan/easysim/'

samps = np.zeros((nsamps, 2*lmax-2, 7))
mean = np.zeros(7)
var = np.zeros(7)
for sampnum in range(nsamps):
    prefix = '/mn/svati/u1/eirikgje/data/commander/chains_titan/easysim/'
    samps[sampnum] = np.loadtxt(prefix + 'cl_c%(chain)04d_k%(samp)05d.dat'%{'chain':chainnum, 'samp':sampnum+1})

for i in range(7):
    mean[i] = np.mean(samps[:, l, i])
    var[i] = np.var(samps[:, l, i])

print mean
print var
corr = np.zeros((nsamps/2, 7))
for i in range(nsamps):
    for n in range(nsamps/2):
        for j in range(7):
            if (i + n < nsamps):
                ind = i+n
            else:
                ind = i+n-nsamps
            corr[n, j] += (samps[i, l, j]-mean[j])/np.sqrt(var[j])*(samps[ind, l, j]-mean[j])/np.sqrt(var[j])

corr = corr/nsamps
x = np.arange(nsamps/2)

plt.figure()
plt.plot(x, corr[:, 1])
plt.figure()
plt.plot(x, corr[:, 2])
plt.figure()
plt.plot(x, corr[:, 4])

