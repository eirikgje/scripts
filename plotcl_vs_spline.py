from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

lmin = 2
lmax = 95
cl = np.loadtxt('orig.dat')
sigma = np.loadtxt('sigma.dat')
spline = np.loadtxt('samp.dat')
#amps_pre = np.loadtxt('firstamps.dat')
nodes_pre = np.loadtxt('spline_nodes.dat', skiprows=1)

#numnodes1= amps_pre[0]
numnodes1= 6
#numnodes2 = amps_pre[numnodes1+1]
numnodes2= 7
#numnodes3 = amps_pre[numnodes1+numnodes2 + 2]
numnodes3= 7

#amps1 = amps_pre[1:numnodes1+1]
#amps2 = amps_pre[numnodes1+2:numnodes1+numnodes2 + 2]
#amps3 = amps_pre[numnodes1+numnodes2+3:]
#nodes1 = nodes_pre[1:numnodes1+1]
#nodes2 = nodes_pre[numnodes1+2:numnodes1+numnodes2 + 2]
#nodes3 = nodes_pre[numnodes1+numnodes2+3:numnodes1+numnodes2+numnodes3+3]

nodes1 = nodes_pre[0:numnodes1]
nodes2 = nodes_pre[numnodes1:numnodes1+numnodes2]
nodes3 = nodes_pre[numnodes1+numnodes2:numnodes1+numnodes2+numnodes3]

plt.plot(cl[lmin-2:lmax-1, 0], cl[lmin-2:lmax-1, 1])
#plt.scatter(nodes1, amps1)
plt.plot(spline[lmin-2:lmax-1, 0], spline[lmin-2:lmax-1, 1])
plt.scatter(sigma[:, 0], sigma[:, 1], c='red')
plt.xscale('log')

plt.figure()
plt.plot(cl[lmin-2:lmax-1, 0], cl[lmin-2:lmax-1, 2])
#plt.scatter(nodes2, amps2)
plt.plot(spline[lmin-2:lmax-1, 0], spline[lmin-2:lmax-1, 2])
plt.scatter(sigma[:, 0], sigma[:, 2], c='red')
plt.xscale('log')

plt.figure()
plt.plot(cl[lmin-2:lmax-1, 0], cl[lmin-2:lmax-1, 3])
#plt.scatter(nodes3, amps3)
plt.plot(spline[lmin-2:lmax-1, 0], spline[lmin-2:lmax-1, 3])
plt.scatter(sigma[:, 0], sigma[:, 3], c='red')
plt.xscale('log')

#plt.figure()
#plt.plot(cl[:, 0], cl[:, 4])
##plt.plot(spline[:, 0], spline[:, 4])
##plt.scatter(sigma[:, 0], sigma[:, 4], c='red')
#plt.xscale('log')
