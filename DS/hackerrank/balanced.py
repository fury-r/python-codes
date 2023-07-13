#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    def node(n,adj,size):
        a=[n]
        w=0
        while a:
            index=a.pop()
            w+=files_size[index]
            if index in adj:
                a.extend(adj[index])
        return w
    adj={}
    edges=[]
    for i,p in enumerate(parent):
        edges.append((p,i))
        if p in adj:
            adj[p].append(i)
        else:
            adj[p]=[i]
    total=sum(files_size)
    diff=sum(files_size)
    for j in edges:
        a,b=j
        adj[a].remove(b)
        c=node(b,adj,files_size)
        diff=min(diff,abs(total-2*c))
        adj[a].append(b)
        print(diff)
    return diff

