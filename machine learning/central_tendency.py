import numpy as np
import statistics
l=[65,55,89,56,35,14,56,55,87,45,92]
l.sort()
def mean(x):
    a=sum(x)/len(x)
    print(a)
def mode(x):
    dict={}
    _max=-10
    m=None
    for i in x:
        if i in dict.keys():
            dict[i]+=1
        else:
            dict[i]=1
    for k,v in dict.items():
        if(v>_max):
            m=k
            _max=v
    print(m)

def median(x):
    if(len(l)%2==0):
        o=round(len(l)/2)
        a=(x[o-1]+x[0])
        print(a)
    else:
        print(x[round(len(l)/2)])
mean(l)
mode(l)
median(l)
