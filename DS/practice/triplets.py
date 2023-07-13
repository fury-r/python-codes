def findTriplets(arr,n):
    result=[]
    for i in arr:
        sub=[i]
        x=i+n
        c=1
        while x in arr and c<3:
            sub.append(x)
            x+=n
            c+=1
        if len(sub)==3:
            result.append(sub)
    print(result)


arr=[1,2,4,5,7,8,10]
findTriplets(arr,3)