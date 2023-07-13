def pageCount(n,p):
    pb = n-p
    turns =[-(-(pb-1)//2) if(n%2!=0) else -(-(pb)//2),-(-(p-1)//2)]
    return min(turns)
print(pageCount(6,5))