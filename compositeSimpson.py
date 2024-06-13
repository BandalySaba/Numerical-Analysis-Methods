import numpy as np

def compositeSimpson(f,a,b,n):
    if n % 2 != 0:
        raise ValueError("n must be an even integer")
        return np.empty()
    
    h = (b - a) / n
    sum_odd = 0
    sum_even = 0

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sum_even += f(x)
        else:
            sum_odd += f(x)
    l = h/3 * (f(a) + f(b) + 4*sum_odd + 2*sum_even)
    return l