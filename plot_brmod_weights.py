from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

filename = '/mn/svati/u1/eirikgje/sandbox/weights_hke_pt1_l11.dat'

weights = np.loadtxt(filename)

weights = np.exp(weights)

x = np.arange(len(weights))

print np.amax(weights)
print np.amin(weights)

plt.semilogy(x, weights)
#plt.plot(x, weights)
#plt.yscale('log')
