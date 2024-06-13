import numpy as np
def newtonDivDiff(xx1,ff1):
    n = len(xx1)
    A = np.empty(shape=((n),(n)))
    A[:,0] = ff1
    
    for i in range(1,n):
        for j in range(1,i+1):
            A[i,j] = (A[i, j - 1] - A[i-1, j - 1]) / (xx1[i] - xx1[i-j])
    FDcoef = A.diagonal()
    BDcoef = A[-1,:]
    return FDcoef, BDcoef