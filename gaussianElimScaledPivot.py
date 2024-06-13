import numpy as np

def gaussianElimScaledPivot(A):
    # find the number of equations
    n,_ = np.shape(A)
    
    # find scale factor for every row
    s = np.max(abs(A[:,:-1]),axis=1) #Take max across columns (axis=1) for each row
    
    # check if there is a row of zeros (some s entries are 0), if so, return a message stating there is no unique solution.
    if any(s==0):
        return "X=No unique solution"

    ## Gaussian Elimination
    # loop through rows
    for i in range(0,n-1):
        # look for the index largest scaled entry in i-th col
        M = abs(A[i:,i])/s[i:]
        p = np.argmax(M) #Tells the index (row) of the largest entry
        
        # if the scaled max entry in i-th col is 0, there is no solution. return a message stating there is no unique solution
        if M[p] ==0:
            return "X=No unique solution"

        # if the scaled max entry is below row i swaping rows i and p
        if p>0:
            A[[i,p+i],:] = A[[p+i,i],:]
            
        # use row operation to zero out the entries below the pivot
        for j in range(i+1,n-1):
            A[j,:] = A[j,:] - A[j,i]/A[i,i]*A[i,:]
    ## backward substitution
    # reserve space for x
    x=np.zeros(n)

    # xn = A(n,n+1)/A(n,n)
    # go backward in rows to solve for x
    # xn = A(n,n+1)/A(n,n)
    for i in range(n-1,-1,-1):
        x[i] = (A[i, -1] - np.dot(A[i, i+1:-1], x[i+1:])) / A[i, i]
    
    # backward substitution, k=n-2,n-3,...,0
    for k in reversed(range(n-1)):
        A[k,-1]-(A[k,k+1:-1].dot(x[k+1:]))/A[k,k]

    return x
