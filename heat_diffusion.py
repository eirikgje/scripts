import numpy as np
from pylab import *
#import matplotlib.pyplot as plt
import time

ion()
hold(False)

#temp = np.zeros((500, 500))
temp = np.zeros((20, 20))
temp[10, 10] = 500.0
#temp[100, 100] = 500.0
#ttemp = np.zeros((500, 500))
ttemp = np.zeros(np.shape(temp))
#times = np.linspace(50.0)
#dt = 0.01
m = imshow(temp, vmin=0, vmax=0.5, interpolation='none')
draw()
time.sleep(0.10)
cx = 0.1
cy = 0.1
for k in range(1000):
    ttemp[:, :] = temp.copy()
    ttemp[:-1, :] += cx * (temp[1:, :] - temp[:-1, :])
    ttemp[1:, :] += cx * (temp[:-1, :] - temp[1:, :])
    ttemp[:, :-1] += cy * (temp[:, 1:] - temp[:, :-1])
    ttemp[:, 1:] += cy * (temp[:, :-1] - temp[:, 1:])
    temp[1:-1, 1:-1] = ttemp[1:-1, 1:-1].copy()
#    temp[250, 250] = 500.0
    temp[0, :] = 0
    temp[-1, :] = 0
    temp[:, 0] = 0
    temp[:, -1] = 0
    m.set_data(temp)
    print np.max(temp)
    draw()
    time.sleep(0.10)

