#!/bin/python3

import math
import os
import random
import re
import sys



import heapq
#
# Complete the 'getMaximumAmount' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY quantity
#  2. INTEGER m
#

def getMaximumAmount(quantity, m):
    s=0
    #using maxheap
    maxheap=[-x for x in quantity]
    heapq.heapify(maxheap)
    for i in range(0,m):
        maxItem=-heapq.heappop(maxheap)
        s+=maxItem
        heapq.heappush(maxheap,-(maxItem-1))
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findOptimalResources(arr, k)

    fptr.write(str(result) + '\n')

    fptr.close()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    quantity_count = int(input().strip())

    quantity = []

    for _ in range(quantity_count):
        quantity_item = int(input().strip())
        quantity.append(quantity_item)

    m = int(input().strip())

    result = getMaximumAmount(quantity, m)

    fptr.write(str(result) + '\n')

    fptr.close()
