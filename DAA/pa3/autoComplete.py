from jmespath import search


class Node:
    def __init__(self,data,level):
        self.data=data
        self.level=level
        self.children=[None]*26
        self.isEnd=False


class Trie:
    def __init__(self):
        self.root=Node('root',0)

    def insert(self,str):
        root=self.root
        for i in str:
            pos=ord(i)-ord('a')
            if root.children[pos]==None:
                root.children[pos]=Node(i,root.level+1)
            root=root.children[pos]
        root.isEnd=True

    def getComplete(self,node,str):

        if node.children.count(None)<26:
            if node.isEnd:
                print(str)
            for i in node.children:
                if  i:
                    self.getComplete(i,str+i.data)
        else:
            print(str)
    def auto_complete(self,str):
        temp=self.root
        search=''
        for i in str:
            pos=ord(i)-ord('a')
            if temp.children[pos]!=None:
                search+=i
                temp=temp.children[pos]
            else:
                break
        node=temp

        self.getComplete(node,search)
       


t=Trie()
p=['min','minimize','max','huff','huffman','huffing']

for i in p:
    t.insert(i)

t.auto_complete('min')
t.auto_complete('hu')