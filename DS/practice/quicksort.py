

def quicksort(arr,l,h):
    if l<h:
        p=partition(arr,l,h)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,h)
        return arr
def partition(arr,l,h):
    index=l
    pivot=arr[index]
    while l<h:
        while l<len(arr) and arr[l]<=pivot:
            l+=1
        while arr[h]>pivot:
            h-=1
        if l<h:arr[l],arr[h]=arr[h],arr[l]
    arr[h],arr[index]=arr[index],arr[h]
    return h
arr = [64, 34, 25, 12, 22, 11, 90]
print(quicksort(arr,0,len(arr)-1))
 
  