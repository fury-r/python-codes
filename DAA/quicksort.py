
from numpy import partition


def quicksort(arr,l,h):
    if l<h:
        mid=partition(arr,l,h)
        quicksort(arr,mid+1,h)
        quicksort(arr,l,mid-1)
        return arr

def partition(arr,l,h):
    index=l
    pivot=arr[index]
    while l<h:
        print(pivot,arr[l],arr[h])

        while l<len(arr) and arr[l]<=pivot:
            l+=1

        while arr[h]>pivot:
            h-=1
        if l<h:arr[l],arr[h]=arr[h],arr[l]
    arr[h],arr[index]=arr[index],arr[h]
    print(h,'return')
    return h
arr=[2,1,4,3,6,5,0]
print(quicksort(arr,0,len(arr)-1))