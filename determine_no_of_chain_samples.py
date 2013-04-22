#! /usr/bin/env python

#import subprocess
#import shlex
import os
import numpy as np

outfile = '/mn/svati/d1/eirikgje/data/spline_project/simulation_data/ctp3_trieste/chain_samples_allreal_allless9_2_burnin40.dat'
chaindir = '/mn/svati/d1/eirikgje/data/spline_project/simulation_data/ctp3_trieste/chains_allreal_allless9_2/'
num_chains_per_real = 10
num_real = 10
burnin = 40

ofile = open(outfile, 'w')
prev = 1
a = os.listdir(chaindir)
for i in range(num_real):
    currnum = 0
    for j in range(num_chains_per_real):
        currchainnum = i * num_real + j + 1
        #subprocess.call(shlex.split('ls -l ' + chaindir + 'cl_c%04d_k* | wc -l | tee temp.log' % currchainnum))
        #list = np.loadtxt('temp.log')
        for file in a:
            if file.startswith('cl_c%04d_k' % currchainnum):
                currnum += 1
#        currnum += list[0] - burnin
        currnum = currnum - burnin
    ofile.write(str(i + 1) + ' ' + str(currnum) + ' ' + str(prev) + ' ' + str(prev + currnum - 1) + '\n')
    prev = prev + currnum

ofile.close()


