def leaders(self, A, N):
    result=[]
    x=A[N-1]
    for i in reversed(range(N-1)):
        if A[i]>=x:
            result.append(x)
            x=A[i]
    result.append(x)
    return result[::-1]