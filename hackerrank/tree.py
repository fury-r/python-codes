class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        self.level=None
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        n=Node(data)
        current=self.root

        if self.root==None: self.root=n
        else:
            while True:
                if data<current.data:
                    if current.left:
                        current=current.left
                    else:
                        current.left=n
                        break
                elif data>current.data:
                    if current.right:
                        current=current.right
                    else: 
                        current.right=n
                        break
                else:
                    break
def preOrder(root):
    l=[]
    tmp=root
    while True:
        print(l)
        if tmp.data not in l:
            l.append(tmp.data)
        elif tmp.data in l and tmp.right.data not in l:
            l.append(tmp.right.data)
            tmp=tmp.right
        elif tmp.data in l and tmp.left.data not in l:
            l.append(tmp.left.data)
            tmp=tmp.left
        else:
            break
    print(l)

t=Tree()
t.insert(1)
t.insert(2)
t.insert(5)
t.insert(6)
t.insert(3)
t.insert(4)
preOrder(t.root)
