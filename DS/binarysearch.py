def search(arr,f,l,r):
    if l<=r:
        mid=l+(r-l)//2



        if arr[mid]==f:
            return True
        elif mid>f:
            return search(arr,f,l,mid-1)
        else:
            return search(arr,f,mid+1,r)
    else:
        return False










l=[ 2, 3, 4, 10, 40 ]
print(search(l,72,0,len(l)-1))
