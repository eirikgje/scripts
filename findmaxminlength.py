from __future__ import division

import tables
import numpy as np

PREFIX = "/mn/svati/d1/eirikgje/data/beams/hdf/"

inF = tables.openFile(PREFIX + "completebeam_30GHz.hdf")

maxlength = 357
minlength = 357
nside = 512

npix = 12*nside**2

for i in range(npix):
    path = "/pix%07d" % i
    tempgroup = inF.getNode(path)
    length = len(tempgroup.listpix)
    if length > maxlength:
        maxlength = length
    if length < minlength:
        minlength = length

print minlength, maxlength

inF.close()
