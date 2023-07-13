import math as m
from itertools import permutations  
def obst(k,f,n):
    k=int(2*(m.factorial(n)/(m.factorial(n)*m.factorial(n-n)))/n+1)
    q= permutations(keys)
    p=[i for i in list(q)]
    print(p,k,n)
    l=[]
    for i in range(0,5):
        a=0
        for j in range(0,len(p[i])):
            w=j+1
            a+=freq[keys.index(p[i][j])]*w
            print(a)
        l.append(a)
    return f"{min(l)} and {l}" 
keys = [10, 20, 30]  
freq = [34, 8, 50]
print(obst(keys,freq,n=len(keys)))
