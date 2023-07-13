def mergesort(left,right):
    l,r=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result+=left[l:]+right[r:]
    return result
def divide(arr):
    if len(arr)<=1:
        return arr
    mid=int(len(arr)/2)
    left,right=divide(arr[:mid]),divide(arr[mid:])
    return mergesort(left,right)
arr=[170,45,75,90,802,24,2,66]
print(divide(arr))
