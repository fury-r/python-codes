def linear(arr,f):
    for i in arr:
        if arr==f:
            return True
    return False
def binary(arr,l,h,f):
    if h>=1 and len(arr)>=h:
        m=l+(h-l)//2
        if arr[m]==f:
            return True
        elif arr[m]>f:
            return binary(arr,l,m-1,f)
        else:
            return binary(arr,m+1,h,f)
    return False
l=[ 2, 3, 4, 10, 40 ]

print(binary(l,0,len(l),10))