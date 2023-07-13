import math


def ntapes(arr,n):
    arr={k:v for k,v in sorted([[k,v] for k,v  in arr.items()],key=lambda item:item[1])}
    tapes={ i+1:[] for i in range(n)}
    sum_of={i+1:0 for i in range(n)}
    c=1
    for k,v in arr.items():
        if c>n:
            c=1
        tapes[c].append(v)
        sum_of[c]+=sum(tapes[c])
        c+=1
    Tr=sum([v for v in sum_of.values()])
    print(f"{tapes}")
    print(f"RT:{Tr}")
    divide= len(arr) if n==1 else n
    print(f"MRT:{math.ceil(Tr/divide)}")
data={
    'L1':10,
    'L2':20,
    'L3':45,
    'L4':70,
    'L5':1,
    'L6':3,
    'L7':7,
    'L8':54,
    'L9':23,
    'L10':67,
 
}
ntapes(data,3)