from __future__ import division
import shlex
import subprocess
import numpy as np

cambcomm = shlex.split("/mn/svati/u1/eirikgje/src/camb/camb paramtau.ini")
rmcomm = shlex.split("rm paramtau.ini")
infile = "WMAP_bestfit_params.ini"
outfile = "paramtau.ini"
normalize_to_C220 = 5408.3

for tau in range(100, 3005, 15):
    subprocess.call(rmcomm)
    taustr = "%04d" % tau
    taudecstr = "%f" % (tau / 10000)
    inf = open(infile, 'r')
    outf = open(outfile, 'w')
    for line in inf:
        if line.startswith("output_root"):
            outf.write("output_root = taucls_c220norm_tau" + taustr + '\n')
        elif line.startswith("re_optical_depth"):
            outf.write("re_optical_depth = " + taudecstr + '\n')
        else:
            outf.write(line)
    inf.close()
    outf.close()
    subprocess.call(cambcomm)
    if normalize_to_C220 > 0:
        a = np.loadtxt('taucls_c220norm_tau' + taustr + '_scalCls.dat')
        fac = normalize_to_C220 / a[218, 1]
        a[:, 1:] = a[:, 1:] * fac
        np.savetxt('taucls_c220norm_tau' + taustr + '_scalCls.dat', a, fmt='%6i %14.5E %14.5E %14.5E')
