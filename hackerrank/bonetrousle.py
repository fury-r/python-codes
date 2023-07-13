import math
import os
import random
import re
import sys
import builtins

def sum(l,r):
    return r*(r+l)

def bonetrousle(n, k, b):
    f=[]
    c=n
    if(sum(1,b)>n or sum(k-b+1,k))<n:
        return -1
    else:
        for i in range(n):
            a=min(k,c-sum(1,b-1))
            f+=[a]
            k-=1
            b-=1
            c-=a
            if(c<=0):
                break
    return  f

if __name__ == "__main__":

    a=int(input().strip())
    for i in range(a):
        f=input().rstrip().split()
        n=int(f[0])
        k=int(f[1])
        b=int(f[2])
        result = bonetrousle(n, k, b)
    
