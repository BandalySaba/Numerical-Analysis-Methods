'''
p (output value) is the approximation of the root of f (x) obtained by Newton’s Method.
f is the function name for the function f (x).
fder is the function name for the the derivative f ′(x) of f (x).
p0 is the initial approximation of the root.
tol is a positive number that indicate the tolerance of the accuracy of the approximation.
maxN is a number that represents the maximum number of iterations allowed
'''

# P_n = P_(n-1) - f(P_(n-1))/f'(P_(n-1))
# To stop, do iter>=maxN or abs(P_n - P_(n-1)) > tol

def newton(f, fder, p0, tol, maxN):
    pold = p0
    pnew = pold - f(pold)/fder(pold)
    n = 1 #iteration
    while ( (n<maxN) ) and ( abs(pnew - pold) > tol ):
        pold = pnew
        pnew = pold - f(pold)/fder(pold)
        n = n + 1
        print('n=', n)
    return pnew, n
