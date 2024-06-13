def fixedpt(g, p0, tol, maxN):
    n=1
    p_new = g(p0)
    while n<maxN and abs(p_new - p0)>tol:
        p_new = p0
        p_new = g(p0)
        n = n + 1
    p = p_new
    print('n=',n)
    return p
