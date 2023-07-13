class Node:
    def __init__(self,data,level):
        self.data=data
        self.level=level
        self.children=[None]*26
        self.isWordEnd=False

class Trie:
    def __init__(self):
        self.root=Node('root',0)

    def insert(self,data):
        root=self.root
        for i in data:
            pos=ord(i)-ord('a')
            if not  root.children[pos]:
                root.children[pos]=Node(i,root.level+1)
            root=root.children[pos]
        root.isWordEnd=True
    def display(self,root,visited):
        print([ i.data for i in root.children if i],'level ',root.level,root.data)

        for i in root.children:
            if i:
                self.display(i,visited)
    def search(self,str):
        root=self.root
        for i in str:
            pos=ord(i)-ord('a')
            if  not root.children[pos]:
                return False
            root=root.children[pos]
        return root.isWordEnd



text='minimize'

t=Trie()
for i in reversed(range(len(text))):
    print(text[i:])
    t.insert(text[i:])

for i in reversed(range(len(text))):
    print(t.search(text[i:]))

    
t.display(t.root,[])