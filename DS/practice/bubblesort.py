def bubblesort(arr):
    swaped=False
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swaped=True
    if swaped:bubblesort(arr)
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubblesort(arr))