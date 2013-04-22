#!/usr/bin/env python
#This version combines samples based on the "new" comm_process_resfiles, where
#the samples are divided into different chains, and the sample numbers are 
#contained in the zeroth element of the sample number dimension. 
#The two sets must have the same number of chains.

import pyfits
import numpy as np

def combine(files, outfile, mode='expand'):
    if mode == 'stack':
        #Outdated now
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

    elif mode == 'expand':
        inithdulist = pyfits.open(files[0])
        hdr = inithdulist[0].header
        numchains = hdr['NUMCHAIN'] * len(files)
        shape = list(inithdulist[0].data.shape)
        shape[1] = numchains
        inithdulist.close()
        max_num_samps = 0
        for file in files:
            currhdulist = pyfits.open(file)
            if currhdulist[0].header['NUMSAMP'] > max_num_samps:
                max_num_samps = currhdulist[0].header['NUMSAMP']
            currhdulist.close()
        shape[0] = max_num_samps + 1
        data = np.zeros(shape)
        for i in range(len(files)):
            currhdulist = pyfits.open(files[i])
            currnumchain = currhdulist[0].header['NUMCHAIN']
            if currnumchain != numchains / len(files):
                raise NotImplementedError()
            currmaxsamps = currhdulist[0].header['NUMSAMP']
            for j in range(currnumchain):
                data[:currmaxsamps + 1, j * len(files) + i] = currhdulist[0].data[:, j]
            currhdulist.close()
        inithdulist = pyfits.open(files[0])
        inithdulist[0].header['NUMSAMP'] = int(max_num_samps)
        inithdulist[0].header['NUMCHAIN'] = int(numchains)
        inithdulist[0].data = data
        inithdulist.writeto(outfile)

files = ('sigma_test6.fits', 'sigma_test7.fits', 'sigma_test7_batch1.fits', 'sigma_test7_batch2.fits')
outfile = 'sigma_test6and7.fits'
combine(files, outfile)
