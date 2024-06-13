def bisection(f, a, b, tol, maxN):
    if (f(a)*f(b)>0):
        print('There may not be a root')
        p=np.NaN
    elif (f(a)*f(b)==0):
        if (f(a)==0):
            p=a
        else:
            p=b
    else:
        iter=0   # iterations
        p=15      # "input some number"
        while (abs(f(p)) > 0)  and (iter < maxN) and (abs(b-a/2) > tol):
            p = (a+b)/2
            if (f(a)*f(b)<0):
                b=p
            else:
                a=p
            iter = iter + 1
    return p
