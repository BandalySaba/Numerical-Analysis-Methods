# MATH 323
# Bandaly Saba 027209531

import cmath 
def mueller(f1, p0, p1, p2, tol, maxN):
    a = (((p1-p2)*(f1(p0)-f1(p2)))-((p0-p2)*(f1(p1)-f1(p2))))/((p0-p2)*(p1-p2)*(p0-p1))
    b = ((((p0-p2)**2)*(f1(p1)-f1(p2)))-(((p1-p2)**2)*(f1(p0)-f1(p2))))/((p0-p2)*(p1-p2)*(p0-p1))
    c = f1(p2)
    if (abs(b+cmath.sqrt((b**2)-4*a*c))) > abs(b-cmath.sqrt((b**2)-4*a*c)):
        E = b+cmath.sqrt((b**2)-4*a*c)
    else:
        E = b-cmath.sqrt((b**2)-4*a*c)
    p=p2-((2*c)/E)
    iter = 1      
    while ((iter<maxN) and abs(p2-p)>tol and abs(f1(p))>0):
        p0=p1
        p1=p2
        p2=p
        a = (((p1-p2)*(f1(p0)-f1(p2)))-((p0-p2)*(f1(p1)-f1(p2))))/((p0-p2)*(p1-p2)*(p0-p1))
        b = ((((p0-p2)**2)*(f1(p1)-f1(p2)))-(((p1-p2)**2)*(f1(p0)-f1(p2))))/((p0-p2)*(p1-p2)*(p0-p1))
        c = f1(p2)
        if abs(b+cmath.sqrt((b**2)-4*a*c)) > abs(b-cmath.sqrt((b**2)-4*a*c)):
            E = b+cmath.sqrt((b**2)-4*a*c)
        else:
            E = b-cmath.sqrt((b**2)-4*a*c)
        p=p2-((2*c)/E)
        iter = iter + 1
    return p, iter
            