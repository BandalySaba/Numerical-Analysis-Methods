#Note that n and m should be even
import numpy as np 

def compSimpson2D(f, a, b, c, d, n, m):
    if n % 2 != 0: #n in x direction
        raise ValueError("n must be an even integer")
        return np.empty()
    if m % 2 != 0: #m in y direction
        raise ValueError("m must be an even integer")
        return np.empty()
    
    h= (b-a)/n
    J1=0 #END terms
    J2=0 #EVEN terms
    J3=0 #ODD terms
    
    #Coefficient values
    for i in range(n+1):
        x=a+i*h
        hy = (d(x)-c(x))/m #m is number of values in y direction
        K1 = f(x,c(x)) + f(x,d(x)) #End terms
        K2 = 0 #Even terms
        K3 = 0 #odd terms
        
        for j in range(1,m,1):
            y = c(x) + j*hy
            if j % 2 == 0:
                K2 = K2 + f(x,y) #Even terms
            else:
                K3 = K3 + f(x,y) #Odd terms
        
        L = (K1 + 2*K2 + 4*K3)*hy/3
        if i == 0 or i == n:
            J1 = J1 + L #end points
        elif i % 2 == 0:
            J2 = J2 + L #Even number
        else:
            J3 = J3 + L #Odd number
        
    J = h*(J1 + 2*J2 + 4*J3)/3
    return J