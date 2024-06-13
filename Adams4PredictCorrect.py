import numpy as np
from RungeKutta4 import RungeKutta4

def Adams4PredictCorrect(f,a,b,alpha,N):
    h = (b-a)/N
    t = np.linspace(a, b, N+1)
    w = np.zeros(N+1)

    _,w[:4] = RungeKutta4(f, a, a+3*h, alpha, 3)
    
    #Adams-Bashforth
    for i in range(3, N):
        w[i+1] = w[i] + (h/24) * (55*f(t[i], w[i]) - 59*f(t[i-1], w[i-1]) + 37*f(t[i-2], w[i-2]) - 9*f(t[i-3], w[i-3]))
        #Adams-Moulton to correct
        w[i+1] = w[i] + (h/24) * (9*f(t[i+1], w[i+1]) + 19*f(t[i], w[i]) - 5*f(t[i-1], w[i-1]) + f(t[i-2], w[i-2]))
    return t, w



