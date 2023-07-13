#Find all pairs with a given sum
def allPairs(self, A, B, N, M, X):
    a=sorted(A)
    b=sorted(B)
    result=[]
    for i in range(N):
        for j in reversed(range(M)):
            if a[i]+b[j]==X:
                result.append([a[i],b[j]])

    return result