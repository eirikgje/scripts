import numpy as np

a = np.loadtxt('planck_binning.dat')
b = np.loadtxt('base_planck_lowl_lowLike_highL.bestfit_cl')

ls = b[:, 0]
Cls = b[:, 1]
lstarts = a[:, 2]
lends = a[:, 3]
binned_noise = []
for lstart, lend in zip(lstarts, lends):
    temp = 0
    if (lstart < 60 and int(lstart) != 32):
        fsky = 0.875
    else:
        fsky = 0.725
    for l in range(int(lstart), int(lend+1)):
        temp += (2.0 * l + 1) / Cls[l-2] ** 2
    binned_noise.append(np.sqrt(2.0 / (fsky ** 2 * temp)))

res = np.array([lstarts, lends, binned_noise])
np.savetxt('binned_cosmic_variance_with_fsky_lowell0875_highell0725.dat', res.T, fmt=('%4d', '%4d', '%10.5e'), delimiter='   ')
