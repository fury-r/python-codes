def selectionsort(arr):
    for i in range(len(arr)):
        m=i
        for j in range(i+1,len(arr)):
            if arr[m]>arr[j]:
                m=j
        arr[i],arr[m]=arr[m],arr[i]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(selectionsort(arr))