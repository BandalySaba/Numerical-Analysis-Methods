import numpy as np

def euler(f, a, b, alpha, N):
    h = (b - a) / N
    t = np.linspace(a, b, N + 1) 
    w = np.zeros(N + 1)
    w[0] = alpha
    for i in range(N):
        w[i + 1] = w[i] + h * f(t[i], w[i])

    return t, w #Arrays