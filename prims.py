def prims(arr):
    n=len(arr)
    counter_list,temp,final=[],[],[]
    temp.append(arr[0][0])
    try:
        for i in range(0,n):
            counter_list=[j[::-1]for j in (arr[i][1])]
            counter_list.sort()
            if counter_list[0][1] not in temp:
                final.append(counter_list[0])
                temp.append(counter_list[0][1])
            else:
                counter_list.pop(0)
                for z in temp:
                    for e in range (len(arr)):
                        if(z==arr[e][0]):
                            break
                    for y in (arr[e][1]):
                        counter_list.append(y[::-1])
                while True:
                    counter_list.sort()
                    if(counter_list[0][1] not in  temp):
                        temp.append(counter_list[0][1])
                        final.append(counter_list[0])
                        break
                    else:
                        counter_list.pop(0)
    except IndexError:
        return f"From {arr[0][0]} {final},{temp}"            
        
arr = [
    ['A',[['F',7],['C',3],['B',5],['B',10]]],
    ['F',[['A',7],['C',8]]],
    ['C',[['F',8],['A',3],['B',6],['D',3]]],
    ['B',[['A',5],['C',6],['E',4],['D',2],['A',10]]],
    ['D',[['B',2],['C',3],['E',2]]],
    ['E',[['B',4],['D',2]]],

]
test = [
    ["A",[["B",4],['H',8]]],
    ["B",[["A",4],["C",8],['H',11]]],
    ["C",[["D",7],['B',8]]],
    ["D",[["C",7],["E",9],['F',14]]],
    ["E",[["D",9],['F',10]]],
    ["F",[["E",10],['G',2]]],
    ["G",[["F",2],['H',1],["I",6]]],
    ["H",[["G",1],['A',8],["I",7]]],
    ["I",[["H",7],['G',6]]]
]
print(prims(arr))