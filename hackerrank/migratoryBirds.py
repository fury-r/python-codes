def migratoryBirds(arr):
    s=set(arr)
    dict={i:arr.count(i) for i in s}
    a=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    return a[0][0]

print(migratoryBirds([1 ,4 ,4 ,4 ,5 ,3,]))