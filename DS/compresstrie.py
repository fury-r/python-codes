class Node:
    def __init__(self,data):
        self.data=data
        self.children=[None]*26
        self.isWordEnd=False
class CompressTrie:
    def __init__(self):
        self.root=Node('*')
        self.node=None
    def getChar(self,data):
        return ord(data)-ord('a')
    def insert(self,data):
        root=self.root
        for i in data:
            pos=self.getChar(i)
            if not  root.children[pos]:
                root.children[pos]=Node(i)
            root=root.children[pos]
        root.isWordEnd=True
    def search(self,data):
        root=self.root
        for i in data:
            pos=self.getChar(i)
            if  root.children[pos]:root=root.children[pos]
            else:
                return False
        return root.isWordEnd

    #not_used
    def compress(self):
        root=self.root
        for i in self.root.children:
            if i.children.count(None)==25:
                l=[x for x in i.children if x]
                i.data+=l[0].data
                i.children=l[0].children
            x=i
            while True:
                for j in x.children:
                    if j.children.count(None)==25:
                        l=[x for x in i.children if j]
                        j.data+=l[0].data
                        j.children=l[0].children
                if j.children.count(None)==26:
                    break
                x=j      
    def getParent(self,root,find):
        for i in root.children:
            if i:
                if find in i.children and find!=i:
                    self.node= i
                self.getParent(i,find)
    def compress_Recursion(self,root):
        if root:
            for i in root.children:
                if i:
                    self.compress_Recursion(i)
                    self.getParent(self.root,i)

                    a=self.node
                    if a:
                        if a!=self.root:
                            if a.children.count(None)==25 or a.children.count(None)==26:
                                a.data+=i.data
                                a.children=list(i.children)
                                a.isWordEnd=i.isWordEnd
                    self.node=None
                                

                
    def data1(self,root):
        if root:
            for i in root.children:
                if i:
                    print(i.data)
                    self.data1(i)





t=CompressTrie()
keys = ["bear","bell","bull","bug",'stock','stop','bid','buy','sell']
#keys = ["bear","big","bell"]

for i in keys:
    t.insert(i)
t.compress_Recursion(t.root)
t.data1(t.root)
        