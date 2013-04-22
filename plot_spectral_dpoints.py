import numpy as np
import matplotlib.pyplot as plt
import fileutils

pix = 9000
a2t = np.array([1.013743, 1.028457, 1.044197, 1.0999, 1.25])
dat = np.array([2451.456787, 1006.207645, 596.2362145, 238.8109685, 126.4624943])
invN = np.array([0.1667824, 0.1453026, 0.169609, 0.1212046, 0.0884299])
mixmat_base = np.array([[1.0, 23.0 / 94.0], [33.0 / 23.0, 33.0 / 94.0], [41.0 / 23.0, 41.0 / 94.0], [61.0 / 23.0, 61.0 / 94.0], [94.0 / 23.0, 1.0]])

fnames = []
nfnames = []
for i in range(5):
    fnames.append('signalmaps_%02d.fits' % (i + 1))
    nfnames.append('invN_%02d.fits' % (i + 1))
frequencies = np.array([23.0, 33.0, 41.0, 61.0, 94.0])
mds = []
nmds = []
for idx, fname in enumerate(fnames):
    mds.append(fileutils.read_file(fnames[idx]))
    nmds.append(fileutils.read_file(nfnames[idx]))

#data = []
#err = []
data = dat
err = 1 / np.sqrt(invN)
#for md, nmd in zip(mds, nmds):
#    data.append(md.map[pix])
#    err.append(1/np.sqrt(nmd.map[pix]))
data = data * a2t
plt.scatter(frequencies, data)
plt.errorbar(frequencies, data, err, fmt=None)
plt.plot(frequencies, a2t * 1445.2627 * mixmat_base[:, 0] ** -3.033717)
plt.plot(frequencies, a2t * 66.74626193 * mixmat_base[:, 1] ** -1.90380762)
plt.plot(frequencies, a2t * (1445.2627 * mixmat_base[:, 0] ** -3.033717 + 66.74626193 * mixmat_base[:, 1] ** -1.90380762))
plt.xscale('log')
plt.yscale('log')
