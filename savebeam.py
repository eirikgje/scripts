from __future__ import division
import numpy as np

def beam_to_fits(filename, beam):
    import pyfits
    cols = pyfits.ColDefs([
        pyfits.Column(name='beam', format='D16.8', array=beam)], tbtype='TableHDU')
    tab = pyfits.new_table(cols, tbtype='TableHDU')
    hdulist = pyfits.HDUList([pyfits.PrimaryHDU(), tab])
    hdulist.writeto(filename)

b = np.loadtxt('eirikbeam.dat')
filename = 'eirikbeam.fits'
beam_to_fits(filename, b)
