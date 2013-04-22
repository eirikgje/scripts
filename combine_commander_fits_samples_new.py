#!/usr/bin/env python
#This version combines samples based on the "new" comm_process_resfiles, where
#the samples are divided into different chains. The two sets must have the
#same number of chains.

import pyfits
import numpy as np

def combine(files, outfile):
    inithdulist = pyfits.open(files[0])
    hdr = inithdulist[0].header
    numchains = hdr['NUMCHAIN']
    curr_num_samp = np.zeros((len(files), numchains))
    inithdulist.close()
    for i in range(len(files)):
        currhdul = pyfits.open(files[i])
        numsamps = currhdul[0].header['NUMSAMP']
        data = currhdul[0].data
        for chain in range(numchains):
            for sample in range(numsamps):
                if np.sum(data[sample + 1, chain]) == 0:
                    curr_num_samp[i, chain] = sample
                    break
        currhdul.close()
    max_num_samps = max(sum(curr_num_samp))
    cum_sum_samps = np.cumsum(curr_num_samp, 0)
    inithdulist = pyfits.open(files[0])
    shape = tuple(inithdulist[0].data.shape[i] if i != 0 else max_num_samps + 1
                  for i in range(len(inithdulist[0].data.shape)))
    data = np.zeros(shape, dtype=inithdulist[0].data.dtype)
    inithdulist.close()
    for i in range(len(files)):
        currhdul = pyfits.open(files[i])
        currdata = currhdul[0].data
        for chain in range(numchains):
            if i == 0:
                data[:cum_sum_samps[i, chain] + 1, chain] = currdata[:curr_num_samp[i, chain] + 1, chain]
            else:
                data[cum_sum_samps[i - 1, chain] + 1:cum_sum_samps[i, chain] + 1, chain] = currdata[1:curr_num_samp[i, chain] + 1, chain]
        currhdul.close()
        
    inithdulist = pyfits.open(files[0])
    inithdulist[0].header['NUMSAMP'] = int(max_num_samps)
    inithdulist[0].data = data
    inithdulist.writeto(outfile)

files = ('test.fits',)
outfile = 'new.fits'
combine(files, outfile)
