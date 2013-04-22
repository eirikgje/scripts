#!/bin/bash

mpirun -n 16 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost eigendecomp testcoadd_invN_after1.unf dummy.unf eigvals_testcoadd_invNafter1.dat
