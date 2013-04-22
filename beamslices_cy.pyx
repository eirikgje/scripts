from __future__ import division

import numpy as np
import tables
import mapmod

cimport numpy as np
cimport cython

@cython.wraparound(False)
@cython.boundscheck(False)
def slice_beam(rows_,
               cols_,
               fname='/mn/svati/d1/eirikgje/data/beams/hdf/tempbeam_30GHz.hdf',
               temponly=True, 
               file_has_temp_only=True, 
               ordering='ring'):
    inF = tables.openFile(fname)
    
    cdef np.ndarray[np.int64_t] rows
    cdef np.ndarray[np.int64_t] cols
    cdef np.ndarray[np.float32_t, ndim=2] out
    cdef np.ndarray[np.float32_t, ndim=3] out_pol

    if isinstance(rows_, int):
        rows_ = [rows_]
    rows = np.asarray(rows_)

    if isinstance(cols_, int):
        cols_ = [cols_]
    cols = np.asarray(cols_)

    if ordering=='ring':
        rows = mapmod.ring2nest_ind(rows, nside=512)
        cols = mapmod.ring2nest_ind(cols, nside=512)
    if temponly:
        out = np.zeros((len(rows), len(cols)), dtype=np.float32)
    else:
        out = np.zeros((len(rows), len(cols), 6), dtype=np.float32)

    cdef np.ndarray[np.float32_t] tmap
    cdef np.ndarray[np.float32_t, ndim=2] tmap_pol
    cdef np.ndarray[np.int32_t] listpix
      
    for i in range(len(rows)):
        path = "/pix%07d" % rows[i] 
        tempgroup = inF.getNode(path)
        if not file_has_temp_only:
            tmap_pol = np.reshape(np.array(tempgroup.map), (-1, 6))
        else:
            tmap = tempgroup.map[:]

        listpix = tempgroup.listpix[:]
        for j in range(len(cols)):
            for k in range(len(listpix)):
                if cols[j] == listpix[k]:
                    if temponly:
                        if file_has_temp_only:
                            out[i, j] = tmap[k]
                        else:
                            out[i, j] = tmap_pol[k, 0]
                    else:
                        out_pol[i, j, :] = tmap_pol[k, :]

    inF.close()
    return out

def get_diags(np.int32_t start, 
              np.int32_t end,
              fname='/mn/svati/d1/eirikgje/data/beams/hdf/tempbeam_30GHz.hdf',
              temponly=True, 
              file_has_temp_only=True, 
              ordering='ring'):

    cdef np.ndarray[np.int32_t] listpix
    if file_has_temp_only:
        temponly = True
    inF = tables.openFile(fname)
    cdef np.ndarray[np.int32_t] min
    cdef np.ndarray[np.int32_t] max
    cdef np.int32_t minwidth
    min = np.zeros(end - start, dtype=np.int32)
    max = np.zeros(end - start, dtype=np.int32)
    min[:] = 12*512**2
    max[:] = 0
    minwidth = 0
    for i in range(start, end):
        currind = i - start
        if ordering == 'ring':
            ind = mapmod.ring2nest_ind(i, nside=512)
        path = "/pix%07d" % ind 
        tempgroup = inF.getNode(path)
        listpix = tempgroup.listpix[:]
        if ordering == 'ring':
            listpix = np.asarray(mapmod.nest2ring_ind(listpix, nside=512),
                                 dtype=np.int32)
        for j in range(len(listpix)):
            if listpix[j] > max[currind]:
                max[currind] = listpix[j]
            if listpix[j] < min[currind]:
                min[currind] = listpix[j]
        if max[currind] - min[currind] > minwidth:
            minwidth = max[currind] - min[currind]

    cdef np.ndarray[np.float32_t, ndim=2] out
    cdef np.ndarray[np.float32_t, ndim=3] out_pol
    if temponly:
        out = np.zeros((end - start, minwidth + 1), dtype=np.float32)
    else:
        out_pol = np.zeros((end - start, minwidth + 1, 6), dtype=np.float32)

    cdef np.ndarray[np.float32_t] tmap
    cdef np.ndarray[np.float32_t, ndim=2] tmap_pol
    cdef np.int32_t matind
    for i in range(start, end):
        matind = i - start
        if ordering == 'ring':
            ind = mapmod.ring2nest_ind(i, nside=512)
        path = "/pix%07d" % ind 
        tempgroup = inF.getNode(path)
        listpix = tempgroup.listpix[:]
        if ordering == 'ring':
            listpix = np.asarray(mapmod.nest2ring_ind(listpix, nside=512),
                                 dtype=np.int32)
        if not file_has_temp_only:
            tmap_pol = np.reshape(np.array(tempgroup.map), (-1, 6))
        else:
            tmap = tempgroup.map[:]
        for j in range(len(listpix)):
            if temponly:
                if file_has_temp_only:
                    out[matind, listpix[j] - min[matind]] = tmap[j]
                else:
                    out[matind, listpix[j] - min[matind]] = tmap_pol[j, 0]
            else:
                out_pol[matind, listpix[j] - min[matind], :] = tmap_pol[j, :]

    inF.close()
    if temponly:
        return out
    else:
        return out_pol
