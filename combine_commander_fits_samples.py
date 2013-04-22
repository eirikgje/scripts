#!/usr/bin/env python

import os
import pyfits
import numpy as np

#prefixlist = ('sigma_worstmap', 'cls_worstmap')
#outfile = ('sigma_worstmap_total.fits', 'cls_worstmap_total.fits')
#prefixlist = ('sigma_worstmap',)
#outfile = ('sigma_worstmap_total.fits',)

samplelists = ['chain_samples_allreal_allless9_burnin40.dat', 'chain_samples_allreal_allless9_2_burnin40.dat']
infilelist = [('sigma_allreal_allless9_burnin40.fits', 'sigma_allreal_allless9_2_burnin40.fits'), ('cls_allreal_allless9_burnin40.fits', 'cls_allreal_allless9_2_burnin40.fits')]
outsamplelist = 'chain_samples_allreal_allless9_total_burnin40.dat'
outfilelist = ['sigma_allreal_allless9_total_burnin40.fits', 'cls_allreal_allless9_total_burnin40.fits']


list = os.listdir('.')
mode = 'mul_real'
num_real=10

if mode == 'single':
    for ofile in outfile:
        if ofile in list:
            os.remove(ofile)
    
    list = os.listdir('.')
    list.sort()
    
    for i in range(len(prefixlist)):
        firstflag = True
        whdu = None
        totsamps = 0
        for file in list:
            if file.startswith(prefixlist[i]):
                hdu = pyfits.open(file)
                if firstflag:
                    data = (np.zeros((0,) + hdu[0].data.shape[1:],
                            dtype=hdu[0].data.dtype))
                    data = np.append(data, hdu[0].data[0].reshape((1,) 
                                    + hdu[0].data.shape[1:]), axis=0)
                    whdu = hdu
                header = hdu[0].header
                data = np.append(data, hdu[0].data[1:], axis=0)
                totsamps += header['NUMSAMP']
                if firstflag:
                    firstflag = False
                else:
                    hdu.close()
        if whdu is not None:
            whdu[0].header['NUMSAMP'] = totsamps
            whdu[0].data = data
            whdu.writeto(outfile[i])
            whdu.close()


elif mode == 'mul_real':
    samples = []
    osamplefile = open(outsamplelist, 'w')
    for i in range(len(samplelists)):
        samples.append(np.loadtxt(samplelists[i]))
    for k in range(len(infilelist)):
        firstflag = True
        fitslist = []
        for file in infilelist[k]:
            fitslist.append(pyfits.open(file))
        data = (np.zeros((0,) + fitslist[0][0].data.shape[1:], 
                dtype=fitslist[0][0].data.dtype))
        data = np.append(data, fitslist[0][0].data[0].reshape((1,) 
                        + fitslist[0][0].data.shape[1:]), axis=0)
        whdu = fitslist[0]
        if k == 0:
            totsamps = 0
            prev = 1
        for i in range(num_real):
            if k == 0:
                currrealsamps = 0
            for j in range(len(fitslist)):
                data = np.append(data, 
                        fitslist[j][0].data[samples[j][i, 2]:samples[j][i, 3] 
                                            + 1], axis=0)
                if k == 0:
                    currrealsamps += samples[j][i, 1]
            if k == 0:
                totsamps += currrealsamps
                osamplefile.write(str(int(i+1)) + ' ' + str(int(currrealsamps)) +
                                    ' ' + str(int(prev)) + ' ' + 
                                    str(int(prev + currrealsamps - 1)) + '\n')
                prev += currrealsamps
        whdu[0].header['NUMSAMP'] = int(totsamps)
        whdu[0].data = data
        whdu.writeto(outfilelist[k])
        whdu.close()

        for hdu in fitslist:
            hdu.close()
