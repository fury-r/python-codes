class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.color = 'R'


class RBT:

    
    def __init__(self):
       self.root = None
       self.flag = 0
       self.flagroot = None
       self.flagnode = None
       self.parent=0
       self.rot = []
    def resetFlag(self):
        self.flag=0
        self.rot=[]
        self.flagroot=None
        self.flagnode=None
        self.parent=0
    def insert(self,root,data):
        if not self.root:
            self.root=Node(data)
            self.root.color='B'
            return self.root
        elif not root:
            return Node(data)
        elif data>root.data:
            a=self.insert(root.right,data)
            if (self.flagroot==a) or (self.flagnode==root and self.flagnode!=None ):
                return a
            else:
                root.right=a
        elif data<root.data:
            a=self.insert(root.left,data)
            if (self.flagroot==a) or (self.flagnode==root and self.flagnode!=None ):
                return a
            else:
                root.left=a
        if self.flag==0:
            if root.data!=data and root.color=='R':
                if root.color=='R' and ((root.left!=None and data<root.data and root.left.color=='R') or (root.right!=None and data>root.data and root.right.color=='R')):
                    parent=self.getparent(self.root,root)
                    if (parent.right!=None and root.data<parent.data and parent.right.color=='R') or (parent.left!=None and root.data>parent.data and parent.left.color=='R'):
                        if data>self.root.data:self.recolor(self.root.right,data)
                        elif data<self.root.data:self.recolor(self.root.left,data)
                    elif (parent.right!=None and root.data<parent.data and parent.right.color=='B') or (parent.left!=None and root.data>parent.data and parent.left.color=='B') or  (parent.right==None and root.data<parent.data  ) or (parent.left==None and root.data>parent.data):
                        self.detectrotation(self.root,data)
                        a=''.join(self.rot[-2:])
                        return self.rotation(parent,a)
        return root
    def recolor(self,root,data):
        if not root:
            return root
        else:
            if data>root.data:
                self.recolor(root.right,data)
            elif data<root.data:
                self.recolor(root.left,data)
            if root.data!=data:
                if root.color=='R':
                    root.color='B'
                elif root.color=='B':
                    root.color='R'
                if self.parent==0:
                    parent=self.getparent(self.root,root)
                    if parent.left:
                        if (root.data>parent.data and parent.left.color=='R'):
                            parent.left.color='B'
                        elif (root.data>parent.data and parent.left.color=='B'):
                            parent.right.color='R'
                    if parent.right:
                        if (root.data<parent.data and parent.right.color=='R'):
                            parent.right.color='B'
                        elif (root.data<parent.data and parent.right.color=='B'):
                            parent.right.color='R'
                    self.parent=1
    def detectrotation(self,root,data):
        if root:
            if data>root.data:
                self.rot.append('R')
                self.detectrotation(root.right,data)
            elif data<root.data:
                self.rot.append('L')
                self.detectrotation(root.left,data)
    def rotation(self,root,rot):
        print(rot,self.rot)
        if rot=='RR':
            return self.LeftRotation(root)
        elif rot=='LR':
            root.left=self.LeftRotation(root.left)
        elif rot=='LL':
            return self.RightRotaion(root)
        elif rot=='RL':
            root.right=self.RightRotaion(root.right)
            return self.LeftRotation(root)
        return root

    def rootcolor(self,root):
        root.color='B'
        if root.right:root.right.color='R'
        if root.left:root.left.color='R'

    def LeftRotation(self,root):
        z=root
        x=root.right
        y=x.left
        x.left=root
        root.right=y
        if self.root==z:
            self.root=x
            self.flagroot=x
            self.flag=1
        self.rootcolor(x)
        self.flagnode=z

        print(x.data,'return')
        return x

    def RightRotaion(self,root):
        z=root
        x=root.left
        y=x.right
        x.right=root
        root.left=y
        if self.root==z:
            self.root=x
            self.flagroot=x
            self.flag=1
        self.rootcolor(x)
        print(x.data,'return')
        self.flagnode=z

        return x
    def Preorder(self,root,pos):
        if root:
            print(root.data,root.color,pos)
            self.Preorder(root.left,'left')
            self.Preorder(root.right,'right')
    def getparent(self,root,search):
        if root:
            if root.left==search or root.right==search:
                return root
            elif search.data>root.data:return self.getparent(root.right,search)
            elif search.data<root.data:return self.getparent(root.left,search)
c=RBT() 
c.root=c.insert(c.root,1)
c.resetFlag()
c.root=c.insert(c.root,3)
c.resetFlag()
c.root=c.insert(c.root,2)
c.resetFlag()
print(c.root)

c.Preorder(c.root,'root')

c.root=c.insert(c.root,4)
c.resetFlag()
c.Preorder(c.root,'root')
print(c.root)
