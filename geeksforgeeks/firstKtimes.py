def firstElementKTime(self,  a, n, k):
    x={
        
    }
    for i in a:
        if i in x.keys():
            x[i]+=1
        else:
            x[i]=1
                
        if x[i]==k:
            return i
    return -1