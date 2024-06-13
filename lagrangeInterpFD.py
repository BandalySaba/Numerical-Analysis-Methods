def lagrangeInterpFD(xx, ff, xp):
    n = len(xx)
    FDcoeff,BDcoeff = newtonDivDiff(xx,ff)
    FDapprox = FDcoeff[0]
    
    for k in range (1,n):
        prod = xp - xx[0]
        for m in range (1,k):
            prod = prod*(xp-xx[m])
        FDapprox = FDapprox + FDcoeff[k]*prod
    return FDapprox