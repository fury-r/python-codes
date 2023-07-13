def MissingNumber(self,array,n):
    array=set(array)
    x=set(range(1,n+1))
    return list((x-array))[0]