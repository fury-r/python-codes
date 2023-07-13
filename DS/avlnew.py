



class Node(object):
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
        self.height=1

class Tree(object):
    def __init__(self):
        self.root=None
        self.level=0
        self.count=0
        self.balance=0
        self.l=[]
    def insert(self,root,data):
        if self.root==None:
            return Node(data)
             
        elif not root:
            return Node(data)
        elif data<root.data:
            print('left')
            root.left=self.insert(root.left,data)
        elif data>root.data:
            print('right')
            root.right=self.insert(root.right,data)
        root.height=1+max(self.get_height(root.left),(self.get_height(root.right)))
        balanceFactor=self.get_height(root.left)-self.get_height(root.right)

        if balanceFactor>1 and data < root.left.data:
            print('RR')
            return self.RightRotation(root)
        if balanceFactor<-1 and data > root.right.data:
            print('LL')

            return self.LeftRotation(root)
        if balanceFactor>1 and data > root.left.data:
            print('LR')


            n=self.LeftRotation(root.left)
            return self.RightRotation(n)   
        if balanceFactor<-1 and data>root.right.data:
            print('RL')

            n=self.RightRotation(root.right)
            return self.LeftRotation(n)                    

        return root
    def get_node(self,root,a):
        if root.left==a or root.right==a:
            return root
        elif root  and a.data>root.data:
            return self.get_node(root.right,a)
        elif root  and a.data<root.data:

            return self.get_node(root.left,a)

    def get_height(self,root):
        if  not root:
                return 0
        else:    
            return  root.height
    def Inorder(self,root):
        if root:
            self.Inorder(root.left)
            print(root.data)
            self.Inorder(root.right)
    def PreOrder(self,root):
        if root:
            print(root.data)
            self.PreOrder(root.left)

            self.PreOrder(root.right)
    #rotations

    def LeftRotation(self,root):
        x=root.right
        y=x.left

        x.left=root
        root.right=y
        print(root.left,root.right)
        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        
        x.height=1+max(self.get_height(x.left),self.get_height(x.right))
        self.root=x
        return x
    def RightRotation(self,root):

        x=root.left
        y=x.right
        x.right=root
        root.left=y
        self.root=x
        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        x.height=1+max(self.get_height(x.left),self.get_height(x.right))
        return x
    def get_balance_post_order(self,root):
        if root:
            a=self.get_height(root)
            
            if a==2:
                self.balance=a 

                x,y,z=root,root.left,root.left
                x.left=z.left
                x.right=z.right
                y.left=x
                y.right=z
                z.right=None
                z.left=None
                self.get_balance_post_order(root.left)
                self.root=y

                return y
            elif a==-2:
                self.balance=a 

                x,y,z=root,root.right,root.right
                x.left=z.left
                x.right=z.right
                y.left=x
                y.right=z
                x.right=None
                x.left=None
                self.get_balance_post_order(root.right)
                self.root=y
                return y
              
c=Tree()
while True:
    op=int(input('1.Add\n2.Display PreOrder\n3.Display InOrder\n4.Display PostOrder\n5.Exit\n'))
    if op==1:
        a=int(input('Data '))
        c.root=c.insert(c.root,a)
  
    elif op==2:
        print('Preorder\n')

        c.PreOrder(c.root)
    elif op==3:
        print('Inorder\n')

        c.Inorder(c.root)
    elif op==4:
        print('Postorder\n')

        c.PostOrder(c.root)
    elif op==5:
        break
                

