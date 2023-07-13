def prims(arr):
    n=len(arr)
    s,w,temp,l=[],[],[],[]
    a=arr[0][1][0]
    temp.append(arr[0][0])
    try:
        for i in range(0,n):
            m,q=[],[]
            w=[j[::-1]for j in (arr[i][1])]
            w.sort()
            if w[0][1] not in temp:
                l.append(w[0])
                temp.append(w[0][1])
            else:
                w.pop(0)
                for z in temp:
                    for e in range (len(arr)):
                        if(z==arr[e][0]):
                            break
                    for y in (arr[e][1]):
                        w.append(y[::-1])
                while True:
                    w.sort()
                    if(w[0][1] not in  temp):
                        temp.append(w[0][1])
                        l.append(w[0])
                        break
                    else:
                        w.pop(0)
    except IndexError:
        print(temp)
        return l            
        
arr = [

    ["A",[["B",7],["C",8]]],
    ["B",[["C",3],["A",7],["D",6]]],
    ["C",[["B",3],["A",8],["D",4],["E",3]]],
    ["D",[["B",6],["C",4],["E",2],["F",5]]],
    ["E",[["D",2],["C",3],["F",2]]],
    ["F",[["D",5],["E",2]]]
]
print(prims(arr))