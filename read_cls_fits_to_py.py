from __future__ import division

import pyfits
import numpy as np

filename = 'cls_ctp3_v2.fits'
outfile = 'cls.npy'

hdulist = pyfits.open(filename)

data = hdulist[0].data

np.save(outfile, data)
