class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        self.height=1



class Tree:
    def __init__(self):
        self.root=None
        self.balance=0
        self.flag=0

    
    def insert(self,root,data):
        if  self.root==None:
            return Node(data)
        elif not root:
            return Node(data)

        elif data<root.data:

            root.left=self.insert(root.left,data)
        elif data>root.data:
            root.right=self.insert(root.right,data)
        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        return self.check_balance(root,data)


    def get_height(self,root):
        if not root:
            return 0
        return root.height
    def check_balance(self,root,data):
        balance=self.get_height(root.left)-self.get_height(root.right)

        if balance<-1 and data>root.right.data:
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
        x=root.right
        y=x.left
        x.left=root
        root.right=y
        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        x.height=1+max(self.get_height(x.left),self.get_height(x.right))
        if self.root==z:
            self.root=x
        return x
    def RightRotation(self,root):
        z=root
        x=root.left
        y=x.right
        x.right=root
        root.left=y
        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        x.height=1+max(self.get_height(root.left),self.get_height(root.right))
        if self.root==z:self.root=x
        return x

    def Preorder(self,root,pos):
        if root:
            print(root.data,pos)
            self.Preorder(root.left,'left')
            self.Preorder(root.right,'right')

c=Tree()
c.root=c.insert(c.root,1)
c.root=c.insert(c.root,2)
c.root=c.insert(c.root,3)
c.root=c.insert(c.root,4)
c.root=c.insert(c.root,5)
c.root=c.insert(c.root,6)

c.Preorder(c.root,'root')
