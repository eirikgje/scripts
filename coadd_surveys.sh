#!/bin/bash

mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost convert_WMAP_to_F90 wmap_band_forered_quninv_r4_7yr_W_v4.fits covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_mK.unf .True.

mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost multiply_by_scalar covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_mK.unf 1.d-6 covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv.unf

mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost invert LU covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv.unf covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask.unf

#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost mask covmat_nside16_wmap_Ka_forered_QUonly_wmapprocessingmask.unf wmap_processing_map2mask_r4_7yr_Ka4_modified.fits wmap_polarization_7yr_mask_IzeroQU.fits covmat_nside16_wmap_Ka_forered_QUonly_wmappolarizationmask.unf wmap_polarization_7yr_map2mask_IzeroQU.fits

#mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost invert LU covmat_nside16_wmap__Wforered_QUonly_wmappolarizationmask.unf covmat_nside16_wmap_W_forered_QUonly_wmappolarizationmask_inv.unf

mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost sqrt covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv.unf covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv

mv covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_sqrt_inv_N.unf covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_sqrt.unf

mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost multiply_by_scalar covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask.unf 41.293129 covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_withsigmasquared.unf

mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost multiply_by_scalar covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv.unf 0.0211447 covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_withsigmasquared.unf

mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost multiply_by_scalar covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_sqrt.unf 0.145412 covmat_nside16_wmap_W_forered_QUonly_wmappolanalysismask_inv_sqrt_withsigmasquared.unf

#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost convert_C_to_F90 covmat_nside32T16_1sec_70GHz_DX9delta_SS5_nopolsmooth_bin.dat 9216 2 3 .false. 2.5d11 0.0d0 covmat_nside16_70GHz_DX9delta_SS5_divby4.unf

#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost convert_C_to_F90 covmat_nside32T16_1sec_70GHz_DX9delta_SS5_nopolsmooth_inv_bin.dat 9216 2 3 .true. 1.d-12 0.0d0 covmat_nside16_70GHz_DX9delta_SS5_inv.unf

#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost add covmat_nside16_70GHz_DX9delta_SS1invplusSS2inv_inv.unf covmat_nside16_70GHz_DX9delta_SS3invplusSS4inv_inv.unf covmat_nside16_70GHz_DX9delta_SS1invplusSS2invinv_plus_SS3invplusSS4invinv.unf

#mpirun -n 1 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost add covmat_nside16_70GHz_DX9delta_SS1plusSS2_divby4.unf covmat_nside16_70GHz_DX9delta_SS3plusSS4_divby4.unf covmat_nside16_70GHz_DX9delta_add1to4_divby4.unf



#mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost invert LU covmat_nside16_70GHz_DX9delta_SS1invplusSS2invinv_plus_SS3invplusSS4invinv.unf covmat_nside16_70GHz_DX9delta_SS1invplusSS2invinv_plus_SS3invplusSS4invinv_inv.unf

#mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost invert LU covmat_nside16_70GHz_DX9delta_SS3plusSS4_divby4_planck_pol_preliminary_mask_s02d02_QUonly.unf covmat_nside16_70GHz_DX9delta_SS3plusSS4_planck_pol_preliminary_mask_s02d02_QUonly_inv.unf


#mpirun -n 10 -machinefile machinefile_owl7.txt ~/src/quiet/quiet_svn/oslo/src/f90/scalapost/scalapost eigendecomp covmat_nside16_70GHz_DX9delta_SS1_planck_pol_preliminary_mask_s02d02_QUonly.unf dummy.unf eigvals_SS1_masked.dat
