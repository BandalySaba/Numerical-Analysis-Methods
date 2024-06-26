import numpy as np

def gaussianQuad(f,a,b,n):
    if n not in [2,3,4,5]:
        raise ValueError('n must be 2,3,4, or 5')
    
    #points are x values
    #weights are coefficients c
    if n == 2:
        points = [-0.577350269189626, 0.577350269189626]
        weights = [1.0, 1.0]
    elif n == 3:
        points = [-0.774596669241483, 0, 0.774596669241483]
        weights = [0.555555555555556, 0.888888888888889, 0.555555555555556]
    elif n == 4:
        points = [-0.861136311594053, -0.339981043584856,
                  0.339981043584856, 0.861136311594053]
        weights = [0.347854845137454, 0.652145154862546,
                   0.652145154862546, 0.347854845137454]
    elif n == 5:
        points = [-0.906179845938664, -0.538469310105683, 0,
                  0.538469310105683, 0.906179845938664]
        weights = [0.236926885056189, 0.478628670499366, 0.568888888888889,
                   0.478628670499366, 0.236926885056189]
    l = 0
    for i in range(n):
        w = ((b-a)/2)*points[i] + (a+b)/2
        l += weights[i] * f(w)
    return (b-a)/2 * l
