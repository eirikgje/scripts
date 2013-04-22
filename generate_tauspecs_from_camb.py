from __future__ import division
import shlex
import subprocess

cambcomm = shlex.split("/mn/svati/u1/eirikgje/src/camb/camb paramtau.ini")
rmcomm = shlex.split("rm paramtau.ini")
infile = "/mn/svati/u1/eirikgje/src/camb/params.ini"
outfile = "paramtau.ini"

for tau in range(415, 1905, 5):
    subprocess.call(rmcomm)
    taustr = "%04d" % tau
    taudecstr = "%f" % (tau / 10000)
    inf = open(infile, 'r')
    outf = open(outfile, 'w')
    for line in inf:
        if line.startswith("output_root"):
            outf.write("output_root = eirikcls_tau" + taustr + '\n')
        elif line.startswith("re_optical_depth"):
            outf.write("re_optical_depth = " + taudecstr + '\n')
        else:
            outf.write(line)

    inf.close()
    outf.close()
    subprocess.call(cambcomm)
