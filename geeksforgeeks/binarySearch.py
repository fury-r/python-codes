import math
def binary( arr,l, h, k):

    if(h>=l):
        if len(arr)<h and (arr[h]==k):
            return h
        if len(arr)>l and (arr[l]==k):
            return l
        mid=(l+h)//2
        if(mid<len(arr)):
            if  (arr[mid]==k):return mid
            elif(arr[mid]>k):
                return binary(arr,l,mid-1,k)
            elif(arr[mid]<k):
                return binary(arr,mid+1,h,k)
        else:
            return -1
    else:
        return -1
def binarysearch( arr, n, k):
	    return binary(arr,0,n,k)
print(binarysearch(list(map(int,"2 3 4 5 7 8 9 11 12 14 15 19 20 22 25 26 28 32 33 35 36 37 38 41 43 44 45 46 49 50 51 52 53 55 59 60 61 62 65 66 67 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 88 92 93 94 95 96 98 99".split(" "))),65,222))