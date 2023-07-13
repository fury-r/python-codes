def longestCommonPrefix(self, arr, n):
    arr=sorted(arr,key=lambda item:len(item))
    
    test=arr[0]
    p=-1
    for i in range(0,len(test)):
        c=0
        while c<len(arr) and test[0:i] in arr[c] :
            c+=1
        if c==len(arr):
            p=test[0:i]
    return p
                
            