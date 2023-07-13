#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    m=0
    print(q)
    q=[p-1 for p in q]
    print(q)
    
    for i,p in enumerate(q):
        print(i,p)
        if(p-i>=3):
            print("Too chaotic")
            return

        for j in range(max(p-1,0),i):
            if q[j] > p:
                m += 1
    print(m)   

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))
        minimumBribes(q[:n])
