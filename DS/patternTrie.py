class Node:
    def __init__(self):
        self.children=[None]*26
        self.isWordEnd=False
class Trie:
    def __init__(self):
        self.root=Node()
    def getChar(self,data):
        return ord(data)-ord('a')
    def insert(self,data):
        root=self.root
        for i in data:
            pos=self.getChar(i)
            if not  root.children[pos]:
                root.children[pos]=Node()
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
    def pattern(self,data):
        root=self.root
        a=''
        l=[]
        for i in data:
            p=self.getChar(i)
            if not root.children[p]:
                return False
            root=root.children[p]
            a=''+root.data
        if root.isWordEnd:
            l.append(a)
        