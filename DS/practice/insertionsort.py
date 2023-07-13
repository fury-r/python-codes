def insertion(arr):
    for i in range (0,len(arr)-1):
        for j in reversed(range(i+1)):
            if j>0:
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion(arr))