#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findOptimalResources' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#
def findOptimalResources(arr, k):
    curr_max=-1
    n=len(arr)
    i=0
    curr_sum=0
    freq={}
    for j in range(n):
        vj=arr[j]

        curr_sum+=vj
        if vj in freq:
            freq[vj]+=1
        else:
            freq[vj]=1
            
        vi=arr[i]
        if j-i+1>k:
            curr_sum-=vi
            freq[vi]-=1
            if freq[vi]==0:
                del freq[vi]
            i+=1
        if len(freq)==k:
            curr_max=max(curr_max,curr_sum)

    return curr_max
