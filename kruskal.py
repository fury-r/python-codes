def kruskal(arr):
    n=len(arr)
    s,w,temp,l=[],[],[],[]
    counter=arr[0][0]
    try:
        temp.append(counter)
        for i in range(0,n):
            print(counter)
            counter_index=[c for c in range(n) if arr[c][0]==counter]
            temp_index=counter_index[0]
            w=[j[::-1]for j in (arr[temp_index][1])]
            print(w)
            w.sort()
            while True:
                if w[0][1] not in temp:
                    temp.append(w[0][1])
                    counter=w[0][1]
                    w[0].reverse()
                    l.append(w[0])
                    break
                else:
                    w.pop(0)
    except IndexError:
        return f"From {arr[0][0]} {l},{temp}"
arr = [

    ["A",[["B",7],["C",8]]],
    ["B",[["C",3],["A",7],["D",6]]],
    ["C",[["B",3],["A",8],["D",4],["E",3]]],
    ["D",[["B",6],["C",4],["E",2],["F",5]]],
    ["E",[["D",2],["C",3],["F",2]]],
    ["F",[["D",5],["E",2]]]
]
ar = [
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
x=[
    ['A',[['F',7],['C',3],['B',5],['B',10]]],
    ['F',[['A',7],['C',8]]],
    ['C',[['F',8],['A',3],['B',6],['D',3]]],
    ['B',[['A',5],['C',6],['E',4],['D',2],['A',10]]],
    ['D',[['B',2],['C',3],['E',2]]],
    ['E',[['B',4],['D',2]]],

]
print(kruskal(x))