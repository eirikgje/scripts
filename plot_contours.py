from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

fname = 'BR_MOD_twopar.dat'

file = open(fname, 'r')

numpoint = file.readline()

numpoint = np.fromstring(numpoint, sep=' ', dtype='int')

file.close()

Q_args = np.zeros(numpoint[0])
N_args = np.zeros(numpoint[1])
lnL = np.zeros((numpoint[0], numpoint[1]))

data = np.loadtxt(fname, skiprows=1)

for i in range(numpoint[0]):
   for j in range(numpoint[1]):
      Q_args[i] = data[i*numpoint[1] + j][0]
      N_args[j] = data[i*numpoint[1] + j][1]
      lnL[i][j] = np.log(data[i*numpoint[1] + j][2])

lnL = -2*(lnL - np.amax(lnL))

my_levels = np.array([0.1, 2.3, 6.17, 11.8])

plt.contour(Q_args, N_args, lnL, my_levels)

