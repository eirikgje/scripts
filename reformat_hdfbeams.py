from __future__ import division

import numpy as np
import tables
import time

#Script to explore various ways of storing data in the hdf files.

PREFIX = "/mn/svati/d1/eirikgje/data/beams/hdf/"
MINLENGTH = 350
MAXLENGTH = 369

inF = tables.openFile(PREFIX + "completebeam_30GHz.hdf")

row_dtype = np.dtype([('beampix', np.int32), ('T', np.float32), ('CT', np.float32), ('ST', np.float32), ('CT2', np.float32), ('CTST', np.float32), ('ST2', np.float32)]) 
info_row_dtype = np.dtype([('start', np.int32), ('length', np.int16), ('nobs', np.float32, (6,))])

tempinfo = np.zeros(1, dtype=info_row_dtype)
for k in range(10):
    t1 = time.time()

    currpos = 0
    outF = tables.openFile(PREFIX + "testbeam%d.hdf" %k, 'w')
    
    filter = tables.Filters(complevel=k, complib='blosc')
    
    beam = outF.createTable(outF.root, 'beam', row_dtype, filters=filter)
    info = outF.createTable(outF.root, 'info', info_row_dtype, filters=filter)
    
    for i in range(1000):
        path = "/pix%07d" % i
        tempgroup = inF.getNode(path)
        length = len(tempgroup.listpix)
        tempinfo['start'] = currpos
        tempinfo['length'] = length
        tempinfo['nobs'] = tempgroup.nobs
    
        tempbeam = np.zeros(length, dtype=row_dtype)
        tempbeam['beampix'] = tempgroup.listpix
        mapholder = np.reshape(np.array(tempgroup.map), (-1, 6))
        j = 0
        for name in 'T CT ST CT2 CTST ST2'.split():
            tempbeam[name] = np.transpose(mapholder)[j]
            j += 1
        currpos += length
    
        beam.append(tempbeam)
        info.append(tempinfo)
    
    outF.close()
    t2 = time.time()
    print k, t2-t1
inF.close()
