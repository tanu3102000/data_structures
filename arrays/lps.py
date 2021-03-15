def lps(A):
    size=len(A)
    L=[[0 for i in range(size)] for i in range(size)]
    for i in range(size):
        L[i][i]=1
    for length in range(2,size+1):
        for i in range(size-length+1):
            j=length+i-1
            if A[i]==A[j] and length==2:
                L[i][j]=2
            elif A[i]==A[j]:
                L[i][j]=2+L[i+1][j-1]
            else:
                L[i][j]=1+max(L[i][j-1],L[i+1][j])
    return L[0][size-1]

A="babbb"
print(lps(A))
