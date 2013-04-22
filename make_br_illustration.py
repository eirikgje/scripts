import matplotlib.pyplot as plt
import numpy as np
import scipy.stats.kde

samps = np.random.randn(300)
samps = np.reshape(samps, (2, 150))
xkern = scipy.stats.kde.gaussian_kde(samps[0])
ykern = scipy.stats.kde.gaussian_kde(samps[1])
x = np.linspace(np.min(samps[0]), np.max(samps[0]))
y = np.linspace(np.min(samps[1]), np.max(samps[1]))

plt.figure()
ax1 = plt.subplot2grid((6, 6), (0, 0), rowspan=5)
plt.plot(ykern(y), y)
plt.ylim(y[0], y[-1])
xlims = ax1.get_xaxis().get_axes().get_xlim()
plt.plot(ax1.get_xaxis().get_axes().get_xlim(), (0.3, 0.3), color='red')
plt.xlim(xlims)
ax2 = plt.subplot2grid((6, 6), (0, 1), rowspan=5, colspan=5)
plt.scatter(samps[0], samps[1], s=150)
plt.scatter(-0.3, 0.3, marker='x', color='r', s=150)
plt.xlim(x[0], x[-1])
plt.ylim(y[0], y[-1])
ax3 = plt.subplot2grid((6, 6), (5, 1), colspan=5)
plt.plot(x, xkern(x))
ylims = ax3.get_yaxis().get_axes().get_ylim()
plt.plot((-0.3, -0.3), ax3.get_yaxis().get_axes().get_ylim(), color='red')
plt.ylim(ylims)
plt.xlim(x[0], x[-1])

plt.subplots_adjust(hspace=0, wspace=0)
ax2.get_yaxis().set_visible(False)
ax2.get_xaxis().set_visible(False)
ax1.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)

plt.savefig('test.png')
plt.savefig('test.eps')

