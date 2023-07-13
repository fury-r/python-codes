def diagonalDifference(arr):
    a=b=q=0
    for i in arr:
        a+=i[q]
        q+=1
    q=-1
    for i in arr:
        b+=i[q]
        q-=1 
    return a-b if(a>b)  else b-a
print(diagonalDifference([[11,2,4],[3,5,6],[10,8,-12]]))