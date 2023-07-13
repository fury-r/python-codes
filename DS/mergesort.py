def mergesort(leftarr,rightarr):
    l,r=0,0
    result=[]
    while l<len(leftarr) and r<len(rightarr):
        if leftarr[l]<rightarr[r]:
            result.append(leftarr[l])
            l+=1
        else:
            result.append(rightarr[r])
            r+=1
    result.extend(leftarr[l:])
    result.extend(rightarr[r:])
    return result
def divide(arr):
    if len(arr)<=1:
        return arr
    m=int(len(arr)/2)
    left,right=divide(arr[:m]),divide(arr[m:])
    return  mergesort(left,right)
arr=[170,45,75,90,802,24,2,66]
print(divide(arr))