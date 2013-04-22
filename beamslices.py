from __future__ import division

import numpy as np
import tables
import mapmod

def slice_beam(rows, cols, fname='/mn/svati/d1/eirikgje/data/beams/hdf/tempbeam_30GHz.hdf', temponly=True, file_has_temp_only=True, ordering='ring'):
    inF = tables.openFile(fname)
    if isinstance(rows, int):
        rows = [rows]
    if isinstance(cols, int):
        cols = [cols]

    if ordering=='ring':
        rows = mapmod.ring2nest_ind(rows, nside=512)
        cols = mapmod.ring2nest_ind(cols, nside=512)
    if temponly:
        out = np.zeros((len(rows), len(cols)))
    else:
        out = np.zeros((len(rows), len(cols), 6))
    for i in range(len(rows)):
        path = "/pix%07d" % rows[i] 
        tempgroup = inF.getNode(path)
        if not file_has_temp_only or not temponly:
            tmap = np.reshape(np.array(tempgroup.map), (-1, 6))

        lpix = tempgroup.listpix[:]
        for j in range(len(cols)):
            if cols[j] in lpix:
                if temponly:
                    if file_has_temp_only:
                        out[i, j] = tempgroup.map[np.where
                                (lpix == cols[j])[0][0]]
                    else:
                        #print np.where(tempgroup.listpix == cols[j])
                        out[i, j] = tmap[np.where
                                        (lpix == cols[j])[0][0], 0]
                else:
                    out[i, j, :] = tmap[np.where
                                        (lpix == cols[j])[0][0], :]
            else:
                if temponly:
                    out[i, j] = 0
                else:
                    out[i, j, :] = 0

    inF.close()
    return out
