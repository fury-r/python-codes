class Node:
    def __init__(self,data):
        self.children=[None]*26
        self.data=data
        self.isWordEnd=False
class Trie:
    def __init__(self):
        self.root=Node('root')
    def insert(self,data):
        root=self.root
        for i in data:
            pos=self.getAlphaPos(i)
            if not root.children[pos]:
                root.children[pos]=Node(i)
            root=root.children[pos]
        root.isWordEnd=True
    def getAlphaPos(self,data):
        return ord(data)-ord('a')
    def search(self,data):
        root=self.root
        for i in data:
            pos=self.getAlphaPos(i)
            if  root.children[pos]:
                root=root.children[pos]
            else:
                return False
        return root.isWordEnd
a=['big','bigger']
t=Trie()
for i in a:
    t.insert(i)
for i in a:
    print(t.search(i))
print(t.root.children[1].children[8].children)