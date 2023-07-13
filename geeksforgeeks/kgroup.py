def reverseInGroups( arr, n, k):
    for i in range(0,n,k):
        arr[i:i+k]=arr[i:i+k][::-1]
    return arr