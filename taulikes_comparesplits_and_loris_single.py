from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

#ASSUMES LMAX IS SET CORRECTLY IN infilenames AND ALL OTHER RELATED FILES!
rmcomm = [shlex.split('rm datasets/br_mod/par.txt'),shlex.split('rm datasets/comm_gauss/par.txt')]
infilenames = ['datasets/br_mod/par_orig.txt', 'datasets/comm_gauss/par_orig.txt']
outfilenames = ['datasets/br_mod/par.txt', 'datasets/comm_gauss/par.txt']
sigmafile = 'sigma_easysim_allless9.fits'
clfile = 'cls_easysim_allless9.fits'
lorisfile = 'loris_slices/tau_slice_0003.dat'
#totnsamps = 1379
#totnsamps = 7574
totnsamps = 10000
redo = True
plot = True
loris = False
editfiles = True
if redo:
    if editfiles:
        #Do all samples first, for comparison with loris
        for comm in rmcomm:
            subprocess.call(comm)
        
        for infile, outfile in zip(infilenames, outfilenames):
            inf = open(infile, 'r')
            outf = open(outfile, 'w')
            for line in inf:
                if (not line.startswith('COMMANDER_FIRST_S') and not 
                        line.startswith('COMMANDER_LAST_S') and not
                        line.startswith('COMMANDER_SIGMAFILE') and not
                        line.startswith('COMMANDER_CLFILE')):
                    outf.write(line)
            inf.close()
            wstring = 'COMMANDER_SIGMAFILE = ' + sigmafile + '\n'
            outf.write(wstring)
            wstring = 'COMMANDER_CLFILE = ' + clfile + '\n'
            outf.write(wstring)
            wstring = 'COMMANDER_FIRST_SAMPLE = 1\n'
            outf.write(wstring)
            wstring = 'COMMANDER_LAST_SAMPLE = ' + str(int(totnsamps)) + '\n'
            outf.write(wstring)
            outf.close()

    subprocess.call(shlex.split('/mn/svati/u1/eirikgje/src/uio_svn/src/flikelihood/src/applications/tauspec_eval/tauspec_eval param_tauspec.txt'))
    temp = np.loadtxt('taulikes.dat')
    np.save('taulikes_all.npy', temp)

    #Do convergence comparison
    if editfiles:
        for i in range(2):
            for comm in rmcomm:
                subprocess.call(comm)
            for infile, outfile in zip(infilenames, outfilenames):
                inf = open(infile, 'r')
                outf = open(outfile, 'w')
                for line in inf:
                    if (not line.startswith('COMMANDER_FIRST_S') and not 
                            line.startswith('COMMANDER_LAST_S') and not
                            line.startswith('COMMANDER_SIGMAFILE') and not
                            line.startswith('COMMANDER_CLFILE')):
                        outf.write(line)
                inf.close()
                wstring = 'COMMANDER_SIGMAFILE = ' + sigmafile + '\n'
                outf.write(wstring)
                wstring = 'COMMANDER_CLFILE = ' + clfile + '\n'
                outf.write(wstring)
                wstring = ('COMMANDER_FIRST_SAMPLE = ' + 
                            str(int(1 + i * totnsamps // 2)) + '\n')
                outf.write(wstring)
                wstring = ('COMMANDER_LAST_SAMPLE = ' + str(int(totnsamps // 2 + 
                                                                i * totnsamps 
                                                                // 2)) + '\n')
                outf.write(wstring)
                outf.close()
            subprocess.call(shlex.split('/mn/svati/u1/eirikgje/src/uio_svn/src/flikelihood/src/applications/tauspec_eval/tauspec_eval param_tauspec.txt'))
            temp = np.loadtxt('taulikes.dat')
            np.save('taulikes_pt' + str(i+1) + '.npy', temp)

if plot:
    if loris:
        lorisspec = np.loadtxt(lorisfile)
    slices = (np.load('taulikes_all.npy'), np.load('taulikes_pt1.npy'), 
              np.load('taulikes_pt2.npy'))
    for slice in slices:
        slice[:, 1] = np.exp(slice[:, 1] - slice[np.argmax(slice[:, 1]), 1])

    plt.figure(1)
    plt.plot(slices[0][:, 0], slices[0][:, 1])
    if loris:
        plt.plot(lorisspec[:, 0], lorisspec[:, 1])
    plt.figure(2)
    plt.plot(slices[1][:, 0], slices[1][:, 1])
    plt.plot(slices[2][:, 0], slices[2][:, 1])

