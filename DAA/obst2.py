import sys

def generate_tree(arr,k_table,main):
    print(arr,'---------')
    if  len(arr)>1:
        divide=k_table[arr[0]][arr[len(arr)-1]-1]
        index=arr.index(divide)
        arr.pop(arr.index(divide))
        tree=[divide]
        c=[arr[:index],arr[index:]]
        print(tree,c,c[1])
        if(len(c[0])>0) and  c[0]!=arr:
            print('calling',c[0])

            tree.extend(generate_tree(c[0],k_table,main))
        if len(c[1])>0 and c[1]!=arr: 
            print('calling',c[1])
            tree.extend(generate_tree(c[1],k_table,main))
            
        return tree
    return arr
def obst(p,q):
    w={i+1:[0 for i in range(len(p))] for i in range(len(p))}
    e={i+1:[0 for i in range(len(p))] for i in range(len(p))}
    z={i+1:[0 for i in range(len(p))] for i in range(len(p))}
    x=len(p)
    for v in range(1,x+1):
        i,j=1,v-1
        while i<x+1 and j<x:
            minsize=sys.maxsize
            min_index=-1
            if (i>j):
                w[i][j]=q[j]
                
                e[i][j]=q[j]
            else:
                w[i][j]=w[i][j-1]+p[j]+q[j]

                for r in range(i,j+1):
                    k=e[i][r-1]+e[r+1][j]+w[i][j]
                    if k<minsize:
                        minsize=k
                        min_index=r
                e[i][j]=minsize
                z[i][j]=min_index

            i+=1
            j+=1 
    nodes=[ i+1 for i in range(x)]
    print("min cost",w[1][-1],e[1][-1],z[1][-1])
    print(generate_tree(nodes,z,nodes,),'-------------')
    for k,v in z.items():
        print(k,v)
arr=[[0,0.15,0.10,0.05,0.10,0.20],[0.05,0.10,0.05,0.05,0.05,0.10]]
obst(arr[0],arr[1])