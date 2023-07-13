class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.height=1

class AVL:
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if not self.root:
            self.root=Node(data)
            return self.root
        elif not root:
            return Node(data)
        elif data>root.data:
            root.right=self.insert(root.right,data)
        elif data<root.data:
            root.left=self.insert(root.left,data)
        root.height=1+max(self.getheight(root.left),self.getheight(root.right))
        return self.checkbalance(root,data)
    
    def getheight(self,root):
        if not root:
            return 0
        return root.height

    def checkbalance(self,root,data):
        balance=self.getheight(root.left)-self.getheight(root.right)
        
        if balance<-1  and data>root.right.data:
            return self.LeftRotation(root)
        elif balance>1 and data>root.left.data:
            root.left=self.LeftRotation(root.left)
            return self.RightRotation(root)
        elif balance>1 and data<root.left.data:
            return self.RightRotation(root)
        elif balance<-1 and data<root.right.data:
            root.right=self.RightRotation(root.right)
            return self.LeftRotation(root)
        return root
    
    def LeftRotation(self,root):
        z=root
        x=z.right
        y=x.left
        x.left=root
        root.right=y

        root.height=1+max(self.getheight(root.left),self.getheight(root.right))
        x.height=1+max(self.getheight(x.left),self.getheight(x.right))
        if self.root==z:
            self.root=x
        return x
    def RightRotation(self,root):
        z=root
        x=root.left
        y=x.right
        x.right=root
        root.left=y
        root.height=1+max(self.getheight(root.left),self.getheight(root.right))
        x.height=1+max(self.getheight(root.left),self.getheight(root.right))
        if self.root==z:self.root=x
        return x
    
    def Preorder(self,root,pos):
        if root:
            print(root.data,pos)
            self.Preorder(root.left,'left')
            self.Preorder(root.right,'right')

c=AVL()
c.root=c.insert(c.root,1)
c.root=c.insert(c.root,2)
c.root=c.insert(c.root,3)

c.root=c.insert(c.root,33)

c.Preorder(c.root,'root')