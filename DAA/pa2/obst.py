

import sys

def generateTee(arr,r,main):

    if len(arr)>1:
        print(arr,len(arr))
        root=r[arr[0]][arr[-1]-1]
        preorder=[root]
        arr.pop(arr.index(root))
        tree={preorder[0]:[arr[:root],arr[root:]]}
        print(preorder,'pre',tree)
        if len(tree[root][0])>0:
            preorder.extend(generateTee(tree[preorder[0]][0],r,main))
        if len(tree[root][1])>0:
            preorder.extend(generateTee(tree[preorder[0]][1],r,main))
        return preorder
    return arr
def obst(p,q):
    w={k+1:[0 for i in range(len(q))] for k in range(len(q))}
    e={k+1:[0 for i in range(len(q))] for k in range(len(q))}
    r={k+1:[0 for i in range(len(q))] for k in range(len(q))}


    for i in range(len(p)):
        x,y=1,i
        while x<len(p)+1 and y<len(p):
            if x>y:
                w[x][y]=q[x-1]
                e[x][y]=q[x-1]
            else:
                w[x][y]=w[x][y-1]+p[y]+q[y]
                min_size=sys.maxsize
                min_index=None

                for k in range(x,y+1):
                    val=e[x][k-1]+e[k+1][y]+w[x][y]
                    if val<min_size:
                        min_size=val
                        min_index=k
                e[x][y]=min_size
                r[x][y]=min_index
            x+=1
            y+=1

    for k,v in r.items():
        print(k,v)
    keys=[i+1 for i in range(len(p)-1)]
    print(generateTee(keys,r,keys))
    print(r)
    print(e)
    print(w[1][-1])                        
arr=[[0,0.15,0.10,0.05,0.10,0.20],[0.05,0.10,0.05,0.05,0.05,0.10]]
obst(arr[0],arr[1])