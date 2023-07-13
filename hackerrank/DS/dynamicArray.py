def dynamicArray(n, queries):
   
    last,arr0,=0,[]
    arr=[[] for i in range(n)]
    for i in queries:
        q=(i[1]^last)%n
        if(i[0]==1):arr[q].append(i[2])
        else:
            p=i[2]%len(arr[q])
            last=arr[q][p]
            arr0.append(last)     
    return arr0 
            
print( dynamicArray(2,[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]) )