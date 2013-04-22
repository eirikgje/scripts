from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import fplcmod

def analytic(fname='taulikes_an.dat', lmax=30):
    anpi = fplcmod.Pluginfo('ANALYTIC', lmin=2, lmax=lmax)
    pis = (anpi,)
    fplcmod.update_files(pis)
    fplcmod.run_program(app='tauspec')
    fplcmod.savefile(fname)

def brcg(fname='taulikes_brcg.dat', lmax=30):
    if lmax > 9:
        brpi = fplcmod.Pluginfo('BR_MOD', lmin=2, lmax=lmax, numranges=2,
                        lranges=(2, 9, lmax), rangetypes=('TT_TE_EE', 'TT'),
                        sigmafile = 'sigma_easysim_allless9.fits')
        cgpi = fplcmod.Pluginfo('COMM_GAUSS', lmin=10, lmax=30, 
                                spectras='TE_EE',
                                clfile='cls_easysim_allless9.fits')
        pis = (brpi, cgpi)
    else:
        brpi = fplcmod.Pluginfo('BR_MOD', lmin=2, lmax=lmax, numranges=1,
                        lranges=(2, lmax), rangetypes=('TT_TE_EE', ))
        pis = (brpi,)
    fplcmod.update_files(pis)
    fplcmod.run_program(app='tauspec')
    fplcmod.savefile(fname)

def plot_output(fname='taulikes.dat'):
    if fname.endswith('npy'):
        data = np.load(fname)
    else:
        data = np.loadtxt(fname)
    data[:, 1] = np.exp(data[:, 1] - data[np.argmax(data[:, 1]), 1])
    p = plt.plot(data[:, 0], data[:, 1])
    return p


def plot_loris(num):
    lorisdata = np.loadtxt(
    '/mn/svati/d1/eirikgje/data/spline_project/slicer_data/ctp3_trieste/loris_slices/tau_slice_%04d.dat' % num)
    p = plt.plot(lorisdata[:, 0], lorisdata[:, 1], c='r')
    return p

