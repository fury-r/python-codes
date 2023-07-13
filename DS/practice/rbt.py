class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = 'R'


class Tree:
    def __init__(self):
        self.root = None
        self.rot = []
        self.flagroot = None
        self.flagnode = None
        self.parent = 0
        self.flag=0
    def insert(self, root, data):
        if self.root == None:
            n = Node(data)
            n.color = 'B'
            self.root = n
            return self.root
        elif not root:
            return Node(data)
        elif data > root.data:
            a = self.insert(root.right, data)


            if self.flagroot == root or (self.flagnode!=None and self.flagnode == root):
                return a
            else:

                root.right = a
        elif data < root.data:
            a = self.insert(root.left, data)
            if self.flagroot == a or (self.flagnode and self.flagnode == root):
                return a
            else:
                if root.left: print(a.data, root.left.data)
                root.left = a
        if self.flag==0:
            if root.data != data and root.color!='B':
                if root.color == 'R' and ((root.right != None and data > root.data and root.right.color == 'R') or (root.left != None and data < root.data and root.left.color == 'R')):
                    parent = self.get_parent(self.root, root)
                    if(parent.left != None and root.data > parent.data and parent.left.color == 'R') or (parent.right != None and root.data < parent.data and parent.right.color == 'R'):
                        print('recolor')
                        if data > root.data:
                            self.recolor(self.root.right, data)
                        else: self.recolor(self.root.left, data)
                    elif(parent.left == None and root.data > parent.data) or (parent.right == None and root.data < parent.data) or (parent.left != None and root.data > parent.data and parent.left.color == 'B') or (parent.right != None and root.data < parent.data and parent.right.color == 'B'):
                        self.detectrotation(parent, data)
                        print(self.rot, root.data)
                        print(self.rot)
                        rot = self.rot[-2]+self.rot[-1]
                        print('rotation ')
                        return self.rotation(parent,rot)

        return root
    def rotation(self, root, rot):
        print(self.rot,rot)
        if rot == 'RR':
            print('in')
            return self.LeftRotation(root)
        elif rot=='RL':
            root.right=self.RightRotation(root.right)
                    
            return self.LeftRotation(root)
        elif rot=='LL':

            return self.RightRotation(root)
        elif rot=='RL':
            root.left=self.LeftRotation(root.left)
                    
            return self.RightRotation(root)
        
    def LeftRotation(self,root):
        z=root
        x=root.right
        y=x.left
        x.left=root
        root.right=y
        if self.root==z:
            print(f'changed root from {self.root.data} to {x.data}')

            self.root=x
            self.flagroot=x
            self.flag=1
        self.rootcolor(x)
        self.flagnode=z

        print('x',x.data,root.data,x.right.data)
        return x
    def RightRotation(self,root):
        z=root
        x=root.left
        y=x.right
        x.right=root
        root.left=y
        self.flagnode=z
        if self.root==z:
            print(f'changed root from {self.root.data} to {x.data}')

            self.root=x
            self.flagroot=x
            self.flag=1

        self.rootcolor(x)
        return x
    def rootcolor(self,root):
        root.color='B'
        if root.right:
            root.right.color='R'
        if root.left:
            root.left.color='R'


    def detectrotation(self,root,search):

        if search>root.data:
            self.rot.append('R')
            self.detectrotation(root.right,search)
        elif search<root.data:
            self.rot.append('L')
            self.detectrotation(root.left,search)
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
                else:
                    root.color='R'
                if self.parent==0:
                    parent=self.get_parent(self.root,root)
                    if (parent.left!=None and  root.data>parent.data and parent.left.color=='R') :
                        parent.left.color='B'

                    elif (parent.right!=None and  root.data<parent.data and parent.right.color=='R'):
                        parent.right.color='B'
                    elif (parent.left!=None and  root.data>parent.data and parent.left.color=='B') :
                        parent.left.color='R'

                    elif (parent.right!=None and  root.data<parent.data and parent.right.color=='B'):
                        parent.right.color='R'
                    self.parent=1
    def get_parent(self,root,search):
        if root:
            if (search.data>root.data and root.right!=None and root.right==search) or (search.data<root.data and root.left!=None and root.left==search):
                return root
            elif search.data>root.data:
                return self.get_parent(root.right,search)
            elif search.data<root.data:
                return self.get_parent(root.left,search)
    def Preorder(self,root,p):
        if root:
            print(root.data,root.color,p)
            self.Preorder(root.left,'Left')
            self.Preorder(root.right,'Right')

    def resetflag(self):
        self.flag=0
        self.flagnode=None
        self.flagroot=None



c=Tree()
c.root=c.insert(c.root,1)
c.resetflag()
c.root=c.insert(c.root,3)
c.resetflag()

c.root=c.insert(c.root,2)
c.resetflag()

c.Preorder(c.root,'root')

c.root=c.insert(c.root,3)
c.resetflag()

c.root=c.insert(c.root,2)
c.root=c.insert(c.root,7)

c.Preorder(c.root,'root')
