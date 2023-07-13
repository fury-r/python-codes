def getMoneySpent(b,k, d):
    a=[ i+j if i+j<=u else -1 for i in k for j in d for u in b]
    return max(a)
print(getMoneySpent([10, 2 ,3],[3,1],[5,2,8]))