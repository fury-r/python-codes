class Node:
    def __init__(self,data):
        self.data=data
        self.children=[None]*26
        self.isWordEnd=False
class CompressedTrie:
    def __init__(self):
        self.root=Node('root')
        self.node=None
    def insert(self,data):
        root=self.root
        for i in data:
            pos=self.getALphaPos(i)
            if not root.children[pos]:
                root.children[pos]=Node(i)
            root=root.children[pos]
        root.isWordEnd=True
    def getALphaPos(self,i):
        return ord(i)-ord('a')
    def getParent(self,root,find):
        for i in root.children:
            if i:
                if find in i.children:
                    self.node= i
                self.getParent(i,find)
    def compress(self,root):
        if root:
            for i in root.children:
                if i:
                    self.compress(i)
                    self.getParent(self.root,i)
                    parent=self.node
                    if  parent and  (parent.children.count(None)==25)  and parent!=self.root:
                        p=[i for i in parent.children if i]
                        p=p[0]
                        if not  parent.isWordEnd:
                            parent.data+=i.data
                            parent.children=list(i.children) 
                            parent.isWordEnd=i.isWordEnd
                        self.node=None
    def display(self,root):
        if root:
            for i in  root.children:
                if i:
                    self.display(i)
                    print(i.data)
                
a=['big','bigger']
t=CompressedTrie()
for i in a:
    t.insert(i)

t.compress(t.root)
t.display(t.root)