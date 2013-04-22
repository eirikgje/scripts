from __future__ import division
import subprocess
import shlex
import os
import fnmatch

def gen_resfiles(relpath=None, suffix='real2_svati.fits', mode=7, maxnum=50000, numchains=1, lmax=90, burnin=0, base_path='/mn/svati/d1/eirikgje/data/spline_project/simulation_data/'):
    if mode != 7 and mode != 1: raise NotImplementedError()
    if relpath is not None:
        path = base_path + relpath
        os.chdir(path)
    fname1 = 'cls_' + suffix
    fname2 = 'sigma_' + suffix

    if mode == 7:
        subprocess.call(shlex.split('/mn/svati/u1/eirikgje/src/uio_svn/src/commander/src/comm_process_resfiles/comm_process_resfiles 7 %s 1 %d %d %d 6 %d' % (fname1, maxnum, numchains, lmax, burnin)))
        subprocess.call(shlex.split('/mn/svati/u1/eirikgje/src/uio_svn/src/commander/src/comm_process_resfiles/comm_process_resfiles 7 %s 2 %d %d %d 6 %d' % (fname2, maxnum, numchains, lmax, burnin)))
    elif mode == 1:
        subprocess.call(shlex.split('/mn/svati/u1/eirikgje/src/uio_svn/src/commander/src/comm_process_resfiles/comm_process_resfiles 1 %s 1 %d %d %d 6 %d' % (fname1, maxnum, numchains, lmax, burnin)))
        subprocess.call(shlex.split('/mn/svati/u1/eirikgje/src/uio_svn/src/commander/src/comm_process_resfiles/comm_process_resfiles 1 %s 2 %d %d %d 6 %d' % (fname2, maxnum, numchains, lmax, burnin)))
    
def cp_resfiles(source_relpath=None, suffix='real2_svati.fits', dest_relpath='ctp3_trieste/', base_source_path='/mn/svati/d1/eirikgje/data/spline_project/simulation_data/', base_dest_path='/mn/svati/d1/eirikgje/data/spline_project/slicer_data/', mode='brcg_new'):
    if source_relpath is not None:
        source_path = base_source_path + source_relpath
    else:
        source_path = ''
    dest_path = base_dest_path + dest_relpath
    f1 = source_path + 'cls_' + suffix
    f2 = source_path + 'sigma_' + suffix
    if mode == 'brcg':
        d1 = dest_path + 'datasets/comm_gauss/'
        d2 = dest_path + 'datasets/br_mod/'
    elif mode == 'brcg_new':
        d1 = dest_path + 'datasets/brcg/'
        d2 = dest_path + 'datasets/brcg/'
    subprocess.call(shlex.split('cp %s %s' % (f1, d1)))
    subprocess.call(shlex.split('cp %s %s' % (f2, d2)))

def gen_cp_resfiles(source_relpath=None, suffix='real2_svati.fits', dest_relpath='ctp3_trieste/', mode=7, maxnum=50000, numchains=1, lmax=90, burnin=0, base_source_path='/mn/svati/d1/eirikgje/data/spline_project/simulation_data/', base_dest_path='/mn/svati/d1/eirikgje/data/spline_project/slicer_data/'):
    gen_resfiles(relpath=source_relpath, suffix=suffix, mode=mode, maxnum=maxnum, numchains=numchains, lmax=lmax, burnin=burnin, base_path=base_source_path)
    cp_resfiles(source_relpath=source_relpath, suffix=suffix, dest_relpath=dest_relpath, base_source_path=base_source_path, base_dest_path=base_dest_path)

#Will make file suffix same as chain directory name. Assumes all directories
#begin with 'chains_'
def gen_cp_resfiles_multipledirs(lsstring, dest_relpath='ctp3_trieste/', mode=1, maxnum=200000, numchains=1, lmax=90, burnin=0, base_source_path='/mn/svati/d1/eirikgje/data/spline_project/simulation_data/', base_dest_path='/mn/svati/d1/eirikgje/data/spline_project/slicer_data/'):
    dirlist = [name for name in os.listdir('.') if os.path.isdir(name)]
    print dirlist
    dirlist = [name for name in dirlist if fnmatch.fnmatch(name, lsstring)]
    basedir = os.path.realpath('.') + '/'
    for dir in dirlist:
        os.chdir(basedir + dir)
        gen_cp_resfiles(suffix=dir[7:] + '.fits', dest_relpath=dest_relpath, mode=mode, maxnum=maxnum, numchains=numchains, lmax=lmax, burnin=burnin, base_source_path=base_source_path, base_dest_path=base_dest_path)
        os.chdir(basedir)
