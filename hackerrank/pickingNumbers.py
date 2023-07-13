def pickingNumbers(a):
    q=[ [i   for i in a for j in a if i>j and i-j<=1],[i   for i in a for j in a if i<j and j-1<=1]]
    if(len(min(q))==0):return  len(max(q))-1
    return len(min(q))-1
print(pickingNumbers([98,3,99,1,97,2]))