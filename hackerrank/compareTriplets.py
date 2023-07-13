def compareTriplets(a,b):
    l=[sum([ 1  for i in range(0,len(a)) if(a[i]>b[i])]),sum([ 1  for i in range(0,len(a)) if(a[i]<b[i])])]
    return l


print(compareTriplets([17, 28, 30],[99,16,8]))