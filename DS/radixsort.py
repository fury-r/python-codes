def radixsort(arr,n):
    strArr=[str(i) for i in arr]
    buckets={

        '0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]
    }
    p=-1
    sort=[]
    for i in range(0,n):
        for j in range(0,len(arr)):
            if len(strArr[j])>i:
                buckets[strArr[j][p]].append(arr[j])
            else:
                buckets['0'].append(arr[j])
        p+=-1
        arr=[]
        for k,v in buckets.items():
            for o in range(len(v)):
                arr.append(v[o])
        buckets={key:[] for key in buckets}
        strArr=[str(i) for i in arr]
        sort=arr
    print(sort)           
arr=[170,45,75,90,802,24,2,66]
radixsort(arr,len(str(max(arr))))