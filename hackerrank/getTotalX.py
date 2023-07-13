def getTotalX(a,b):
    m=max(a)
    n=min(b)
    c=0
    for i in range(m,n+1):
        if(all([i%j==0 for j in a])):
            if(all([j%i==0 for j in b])):
                c+=1
    l=[ 1 if(all([j%i==0 for j in b])) else 0  for i in range(m,n+1)  if(all([i%j==0 for j in a]))]
    return sum(l)
print(getTotalX([3,4],[24,36]))