def naturalSpline(xx,ff):
    n = len(xx) - 1
    a = ff
    h = xx[1:] - xx[0:-1]
    
    maindiag = (np.concatenate(([1], (2*(h[0:-1]+h[1:])), [1])))
    diagabove = (np.concatenate(([0], h[1:])))
    diagbelow = (np.concatenate((h[0:-1],[0])))
    A = np.diag(maindiag) + np.diag(diagabove,1) + np.diag(diagbelow, -1)

    p = np.concatenate(([0], (3/h[1:])*(a[2:]-a[1:-1]) - (3/h[0:-1])*(a[1:-1]-a[0:-2]) ,[0]))
    w = np.linalg.solve(A,p)

    b = np.zeros(n)
    b = ((a[1:] - a[:-1]) / h) - ((h * (w[1:] + 2*w[:-1])) / 3)

    d = (w[1:] - w[:-1]) / (3 * h)
    a = a[0:-1]
    c = w[0:-1]
    return a, b, c, d
