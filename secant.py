'''
p is the approximation of the root of f (x) obtained by the Secant Method.
f is the function name for the function f (x).
p0, p1 are the initial approximations p0 and p1.
tol is a positive number that indicate the tolerance of the approximation.
maxN is a number that represents the maximum number of iterations allowed
'''


def secant(f, p0, p1, tol, maxN):
    polder = p0 #p_(n-2)
    pold = p1  #p_(n-1)
    pnew = pold - ( f(pold)*(polder-pold) )/( f(polder)-f(pold) )
    n = 1 #iteration
    while ( (n<maxN) ) and ( abs(pnew - pold) > tol ):
        polder = pold
        pold = pnew
        pnew = pold - ( f(pold)*(polder-pold) )/( f(polder)-f(pold) )
        n = n + 1
        print('n=', n)
    return pnew

    