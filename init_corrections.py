import numpy as np

def refine_initcorr(f_nu):
    N_0 = 0.5
    psicurr = 1.0
    for i in xrange(100):
        psinew = - (1 + 0.8 * f_nu * N_0) / (0.8 * f_nu + 1)
        N_0 = - 0.5 * psinew
        psicurr = psinew
        print 'psicurr', psicurr
        print 'N_0', N_0
