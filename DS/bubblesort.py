def bubblesort(arr):
    a=0
    z=sorted(list(arr))
    for i in arr:
        if z!=arr:
            for j in arr:
                if i>j and arr.index(j)>arr.index(i):
                    a=arr.index(i)
                    b=arr.index(j)
                    arr[a],arr[b]=j,i
            a+=1
    print(arr,a)     





a=[5,1,4,2,8]
bubblesort(a)