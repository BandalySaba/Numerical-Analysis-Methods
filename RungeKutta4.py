import numpy as np 

def RungeKutta4(f,a,b,alpha,N):

    h = (b-a)/N
    t = np.linspace(a,b,N+1)
    w = np.zeros(N+1)
    w[0] = alpha
    
    for i in range(1,N+1):
        k1 = h*f(t[i-1],w[i-1])
        k2 = h*f(t[i-1] + h/2, w[i-1] + k1/2)
        k3 = h*f(t[i-1] + h/2, w[i-1] + k2/2)
        k4 = h*f(t[i-1] + h, w[i-1] + k3)
        
        w[i] = w[i-1] + (k1+2*k2+2*k3+k4)/6        
    return t,w