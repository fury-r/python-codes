def sort__merge(l,r):
    x=[]
    i=0
    j=0
    while i<len(l) and j<len(r):
        if l[i]>=r[j]:
            x.append(r[j])
            j+=1
        else:
            x.append(l[i])
            i+=1
    x.extend(l[i:])
    x.extend(r[j:])
    return x
def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=merge(arr[:mid])
        r=merge(arr[mid:])
        return sort__merge(l,r)
    else:
        return arr

print(merge([0,2,1,2,0]))
