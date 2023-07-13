def performOperations(arr, operations):
    for i,j in operations:
       # print(arr[:i],arr[i:j+1][::-1],arr[j+1:],f"{i}-{j}")

        arr=arr[:i]+arr[i:j+1][::-1]+arr[j+1:]
    return arr
