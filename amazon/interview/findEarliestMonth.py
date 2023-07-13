#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findEarliestMonth' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY stockPrice as parameter.
#

def findEarliestMonth(stockPrice):
    low=[sys.maxsize,sys.maxsize]
    for i in range(0,len(stockPrice)-1):
        start=math.floor(sum(stockPrice[:i+1])/(len(stockPrice[:i+1])))

        end=math.floor(sum(stockPrice[i+1:])/(len(stockPrice[i+1:])))

        avg=abs(start-end)
        if low[1]>avg:
            low=[i+1,avg]
    return low[0]
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockPrice_count = int(input().strip())

    stockPrice = []

    for _ in range(stockPrice_count):
        stockPrice_item = int(input().strip())
        stockPrice.append(stockPrice_item)

    result = findEarliestMonth(stockPrice)

    fptr.write(str(result) + '\n')

    fptr.close()
