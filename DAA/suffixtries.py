class Node:
    def __init__(self,value,level):
        self.value=value
        self.children=[None]*26
        self.isWordEnd=False
        self.level=level


class Trie:
    def __init__(self):
        self.root=Node('root',0)
    def insert(self,data):
        print(data)
        root=self.root
        for i in data:  
            ch=ord(i)-ord('a')
            if root.children[ch]==None:
                root.children[ch]=Node(i,root.level+1)
            root=root.children[ch]
        root.isWordEnd=True
    
    def search(self,data):
        root=self.root
        for i in data:        
            ch=ord(i)-ord('a')
            if  not root.children[ch]:
                return False
            else:
                root=root.children[ch]
        return root.isWordEnd              

    def display(self,root):
        print(f"Children of {root.value} level {root.level}")
        print(f"Children  {[i.value  for i in root.children if i ]}")

        for i in root.children:
            if i:
                self.display(i)

        

x='minimize'

t=Trie()

for i in reversed(range(len(x))):
    t.insert(x[i:])

for i in reversed(range(len(x))):
    print(t.search(x[i:]))

t.display(t.root)