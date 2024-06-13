def hermiteDivDiff(xx, ff, ffd):
    n = len(xx) #Number of x points (n+1)
    B = np.zeros((2*n, 2*n)) #Reserve space for B
    Z = np.zeros(2*n) #Make Z array
    
    #Fill in x's for Z array
    Z[0::2] = xx 
    Z[1::2] = xx
    #Fill ff's in the 0th column of B
    B[0::2,0] = ff
    B[1::2,0] = ff
                 
    #1st column of B
    B[1::2,1] = ffd
    #Rest of 1st column of B with 1st DD
    for i in range(2, 2*n, 2): #DD from Newtonss DivDiff
        for j in range(1,i+1):
            B[i,j] = (B[i, j - 1] - B[i-1, j - 1]) / (Z[i] - Z[i-j])
    #Rest of B
    for i in range(2,2*n):
        for j in range(2,i+1):
            B[i,j] = (B[i, j - 1] - B[i-1, j - 1]) / (Z[i] - Z[i-j])
    
    #Diagonal of B is output
    Hcoeff = B.diagonal()
    return Hcoeff