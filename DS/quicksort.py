def quicksort(arr,l,h):
    if (l<h):
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
  
def partitionlast(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1        

arr=[170,45,75,90,802,24,2,66]
print(quicksort(arr,0,len(arr)-1))


