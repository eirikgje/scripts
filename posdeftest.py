from __future__ import division
import numpy as np
from numpy import linalg as LA

cls = np.loadtxt('brcls.dat')

mat = np.zeros((2, 2))

for l in range(len(cls[:, 0])):
    mat[0, 0] = cls[l, 1]
    mat[0, 1] = cls[l, 3]
    mat[1, 0] = mat[0, 1]
    mat[1, 1] = cls[l, 2]
    eig, vecs = LA.eig(mat)
    for i in range(len(eig)):
        if eig[i] <= 0:
            print l

