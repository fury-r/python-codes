def prims(arr):
    n=len(arr)
    v,node,used_node,c=0,[],[],[]
    
    used_node.append(arr[0][0])
    try:

        for i in range(0,n):
            node=[j[::-1]for j in (arr[i][1])]
            node.sort()

            if node[0][1] not in used_node:
                c.append(node[0])
                used_node.append(node[0][1])
                

            else:
                node.pop(0)
                for x in used_node:
                    for y in range (len(arr)):
                        if(x==arr[y][0]):
                            break
                    for z in (arr[y][1]):
                        node.append(z[::-1])
                        
                    

                while True:
                    node.sort()
                    if(node[0][1] not in  used_node):
                        used_node.append(node[0][1])
                        
        
                        c.append(node[0])

                        
                        

                        
                        
                        break
                    else:
                        node.pop(0)
                        
    except IndexError:
        
        
        for a in range (0,len(used_node)):
            if a!=5:
                print("From "+used_node[a],"to",c[a][1],"=",c[a][0])
                v+=c[a][0]
        return v
arr = [

    ["A",[["B",7],["C",8]]],
    ["B",[["C",3],["A",7],["D",6]]],
    ["C",[["B",3],["A",8],["D",4],["E",3]]],
    ["D",[["B",6],["C",4],["E",2],["F",5]]],
    ["E",[["D",2],["C",3],["F",2]]],
    ["F",[["D",5],["E",2]]]
]
print(prims(arr))