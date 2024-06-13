# this function does Gaussian Elimination on the augmented matrix A
# and use backward substitution to solve the system
# 5/1/2024
# Bandaly Saba

import numpy as np

def gaussianElim(A):
    # find the number of equations; Take the number of rows from A.shape
    n,_ = np.shape(A)
    
    ## Gaussian Elimination
    # goint through rows for loop through rows i = 0:n-1
    # find the first nonzero entry in the i-th column from a_ii to a_ni
    for i in range(0,n-1): 
        p_all = np.nonzero(A[i:,i])[0] #Gives all indices of the nonzero entries
        p = p_all[0]
        
        # if there is no nonzero entry, make x = message about no unique solution
        if p_all.size==0:
            return "X=No unique solution"
        
        # if the nonzero entry is not at a_ii (p is positive; p>0), swap row i and p+i
        if p > 0:
            A[[i,p+i],:] = A[[p+i,i],:] #Swap rows: A[[i,p+i],:] = A[[p+i,i],:]
 
        # do row operations to zero out the entries below a_ii
        # For loop j=i+1:n-1, E_j <= E_j - a_{ji}/a_{ii}*E{i}
        for j in range(i+1,n):
            A[j,:] = A[j,:] - (A[j,i]/A[i,i])*A[i,:]
    
    ## Backward Substitution; **Same for other function
    
    # reserve space for x
    x=np.zeros(n)
    
    # xn = A(n,n+1)/A(n,n)
    for i in range(n-1,-1,-1):
        x[i] = (A[i, -1] - np.dot(A[i, i+1:-1], x[i+1:])) / A[i, i]
    
    # backward substitution, k=n-2,n-3,...,0
    for k in reversed(range(n-1)):
        A[k,-1]-(A[k,k+1:-1].dot(x[k+1:]))/A[k,k]
    
    return x