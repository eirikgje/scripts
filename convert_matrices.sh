#!/bin/bash

mpirun -n 1 -machinefile machinefile_owl8.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost convert_C_to_F90 ffp6_ncm_143_nominal_covmat_block_nside16.bin 9216 2 3 .false. 1.d12 0.0d0 covmat_nside16_143GHz_FFP6_nom.unf

mpirun -n 1 -machinefile machinefile_owl8.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost mask covmat_nside16_143GHz_FFP6_nom.unf map2mask_fullsky_n16_nested.fits planck_pol_mask_preliminary_n16_s02d02_QUonly.fits covmat_nside16_143GHz_FFP6_nom_planck_pol_preliminary_mask_s02d02.unf outmap2mask.fits

mpirun -n 10 -machinefile machinefile_owl8.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost invert LU covmat_nside16_143GHz_FFP6_nom_planck_pol_preliminary_mask_s02d02.unf covmat_nside16_143GHz_FFP6_nom_planck_pol_preliminary_mask_s02d02_inv.unf

mpirun -n 10 -machinefile machinefile_owl8.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost sqrt covmat_nside16_143GHz_FFP6_nom_planck_pol_preliminary_mask_s02d02_inv.unf 143nominvsqrt

mv 143nominvsqrt_sqrt_inv_N.unf covmat_nside16_143GHz_FFP6_nom_planck_pol_preliminary_mask_s02d02_inv_sqrt.unf
#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost convert_WMAP_to_F90 wmap_band_forered_quninv_r4_7yr_W_v4.fits covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_mK.unf .True.
#
#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost multiply_by_scalar covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_mK.unf 1.d-6 covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv.unf
#


#mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost invert LU covmat_nside16_wmap__Wforered_QUonly_wmappolarizationmask.unf covmat_nside16_wmap_W_forered_QUonly_wmappolarizationmask_inv.unf



#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost multiply_by_scalar covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask.unf 41.293129 covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_withsigmasquared.unf

#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost multiply_by_scalar covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv.unf 0.0211447 covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_withsigmasquared.unf

#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost multiply_by_scalar covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_sqrt.unf 0.145412 covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_sqrt_withsigmasquared.unf


#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost convert_C_to_F90 covmat_nside32T16_1sec_70GHz_DX9delta_SS5_nopolsmooth_inv_bin.dat 9216 2 3 .true. 1.d-12 0.0d0 covmat_nside16_70GHz_DX9delta_SS5_inv.unf

#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost add covmat_nside16_70GHz_DX9delta_SS1invplusSS2inv_inv.unf covmat_nside16_70GHz_DX9delta_SS3invplusSS4inv_inv.unf covmat_nside16_70GHz_DX9delta_SS1invplusSS2invinv_plus_SS3invplusSS4invinv.unf

#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost add covmat_nside16_70GHz_DX9delta_SS1plusSS2_divby4.unf covmat_nside16_70GHz_DX9delta_SS3plusSS4_divby4.unf covmat_nside16_70GHz_DX9delta_add1to4_divby4.unf



#mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost invert LU covmat_nside16_70GHz_DX9delta_SS1invplusSS2invinv_plus_SS3invplusSS4invinv.unf covmat_nside16_70GHz_DX9delta_SS1invplusSS2invinv_plus_SS3invplusSS4invinv_inv.unf

#mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost invert LU covmat_nside16_70GHz_DX9delta_SS3plusSS4_divby4_planck_pol_preliminary_mask_s02d02_QUonly.unf covmat_nside16_70GHz_DX9delta_SS3plusSS4_planck_pol_preliminary_mask_s02d02_QUonly_inv.unf


#mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost eigendecomp covmat_nside16_70GHz_DX9delta_SS1_planck_pol_preliminary_mask_s02d02_QUonly.unf dummy.unf eigvals_SS1_masked.dat
