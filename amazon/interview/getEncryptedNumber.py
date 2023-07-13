#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getEncryptedNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def getEncryptedNumber(numbers):
    if len(numbers)==2:
        return "".join([str(i) for i in numbers])

    while len(numbers)!=2:
        temp=[]

        for i in range(len(numbers)-1):
            a=int(numbers[i])+int(numbers[i+1])
            
            if a>9:
                a=str(a)[1]
            else:
                a=str(a)
            temp.append(a)
        numbers=temp
    
    return "".join(numbers)
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = getEncryptedNumber(numbers)

    fptr.write(result + '\n')

    fptr.close()
