def lenOfLongSubarr ( arr, n, k) : 
    
    point=0
    point1=1
    result=[]
    while point<n and point1<n:
        x=arr[point:point1]
        print(x,sum(x))
        if sum(x)==k and len(x)>len(result):
            result=x
            point+=1
            point1+=1
        elif sum(x)>k:
            point+=1
        else:
            point1+=1
    if len(result)==0:
        return 0
    return len(result)
              
    
print(lenOfLongSubarr(list(map(int,'-13 0 6 15 16 2 15 -12 17 -16 0 -3 19 -3 2 -9 -6'.split(' '))),17 ,15))