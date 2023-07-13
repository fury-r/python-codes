import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,root,data):
        #print(data)
        if not self.root:
            self.root=Node(data)
        
        elif not root:
            return Node(data)
        elif data>root.data:
            root.right=self.insert(root.right,data)
        elif data<root.data:
            root.left=self.insert(root.left,data)
        return root    
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
def generate_tree(arr,k_table,main):
    if  len(arr)>0:
        divide=k_table[arr[0]][arr[len(arr)-1]]
        index=arr.index(divide)
        arr.pop(arr.index(divide))
        pos=[arr[:index],arr[index:]]
        tree={divide:[arr[:index],arr[index:]]}
        preorder=[divide]
        if(len(tree[divide][0])>0):
            #tree[divide][0]=generate_tree(tree[divide][0],k_table,main)
            preorder.extend(generate_tree(tree[divide][0],k_table,main))
        if len(tree[divide][1])>0: 
            #tree[divide][1]=generate_tree(tree[divide][1],k_table,main)
            preorder.extend(generate_tree(tree[divide][1],k_table,main))
        return preorder
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
    nodes=[ i+1 for i in range(x-1)]
    print("min cost",w[1][-1],e[1][-1],z[1][-1])

    preorder=generate_tree(nodes,z,nodes,)
    print("\nW table")
    for k,v in w.items():
        print(k,v)
    print("\nE table")
    for k,v in e.items():
        print(k,v)
    print("\nR table")

    for k,v in z.items():
        print(k,v)
    return preorder
arr=[[0,0.15,0.10,0.05,0.10,0.20],[0.05,0.10,0.05,0.05,0.05,0.10]]
preorder=obst(arr[0],arr[1])

print(preorder)

t=Tree()

for i in preorder:
    t.insert(t.root,i)
t.preorder(t.root)