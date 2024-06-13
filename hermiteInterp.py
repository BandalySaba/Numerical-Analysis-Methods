def hermiteInterp(xx,ff,ffd,xp):
    n = len(xx)
    z = np.zeros(2*n)
    z[0::2] = xx
    z[1::2] = xx
    Hcoeff = hermiteDivDiff(xx,ff,ffd)
    Happrox = Hcoeff[0]
    for k in range(1,2*n):
        prod = xp - z[0]
        for m in range(1,k):
            prod = prod*(xp-z[m])
        Happrox = Happrox + Hcoeff[k]*prod
    return Happrox