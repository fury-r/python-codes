

from turtle import st


def distinct_difference(l,n):
    result=[]
    for i in range(n):
        x=len(set([k for k in l[:i] if k<=l[i]]))-len(set([k for k in l[i+1:] if k>=l[i]]))
        result.append(x)
    print(result)



distinct_difference([4,3,3],3)