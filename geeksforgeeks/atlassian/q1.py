from audioop import reverse


def SmallestTower(arr):
    result=[]
    temp=sorted(arr)
    for i in arr:
         
        if temp[0]<i:
            y=temp.index(i)
            l=[]
            d=temp[:y]
            print(d,y,i)
            for p in d:
                if arr.index(p)>arr.index(i):
                    l.append([arr.index(p)-arr.index(i),arr.index(p)])
                else:
                    l.append([arr.index(i)-arr.index(p),arr.index(p)])
            l=sorted(l)
            result.append(l[0][1])


                
        elif i==temp[0]:
            result.append(-1)
    return result

p='4 8 6 5 3'
p=list(map(int,p.split(' ')))
print(SmallestTower(p))