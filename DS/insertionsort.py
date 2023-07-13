def insertionsort(arr):
    for i in range(0, len(arr)):
        k = arr[i]
        j = i-1
        while j >= 0 and k < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j+1] = k
    return arr


def insertion(arr):

    for i in range(len(arr)):
        k=arr[i]
        j=i-1
        while j>=0 and k<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=k
    return arr

arr=[64,25,12,22,11]
print(insertionsort(arr)) 
print(insertion(arr)) 