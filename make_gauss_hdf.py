from __future__ import division

#On hold until query_disc is wrapped

import numpy as np
import tables
import healpix as heal

def gaussbeam_al0(l):
    return np.sqrt((2*l+1)/(4*np.pi))*np.exp(-l*(l+1)*sigma*sigma/2)

#Radius in multiples of FWHM, given by 2*pixsize.
def makebeam(nside, pix, radius, ordering='nest'):

