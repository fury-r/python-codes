def selectionsort(arr,l,h):
    if len(arr)==l:
        return arr
    o=arr[l]
    for i in  range( l,h):
        if o>arr[i]:
            o=arr[i]
    p=arr.index(o)
    arr[l],arr[p]=o,arr[l]
    return selectionsort(arr,l+1,h)
arr=[64,25,12,22,11]
print(selectionsort(arr,0,len(arr)))