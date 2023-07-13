def rotLeft(a, d):
    return a[d:]+a[:d]
    
print(rotLeft([1,2,3,4,5],3))