



class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
        self.height=1

class Tree:
    def __init__(self):
        self.root=None
        self.level=0
        self.count=0
        self.balance=0
        self.l=[]
    #iterative
    def insert_iterative(self,data):
        if self.root==None:
            self.root=Node(data)
            self.level=0
        else:
            tmp=self.root
            c=0
            while True:
                
                if tmp.data==data:return 'It already exists!!!!'
                if data>tmp.data and tmp.right==None:
                    print('in right')
                    tmp.right=Node(data)
                    break
                elif data<tmp.data and tmp.left==None:
                    print('in left')

                    tmp.left=Node(data)
                    if c>self.level:self.level=c
                    break
                elif data>tmp.data  and tmp.right!=None: 
                    print('in right')

                    tmp=tmp.right
                    if c>self.level:self.level=c

                elif data<tmp.data and tmp.left!=None:
                    print('in left')

                    tmp=tmp.left

                else:
                    break
                
        self.checkBalance_iterative(self.root,data)
    def  get_height_iterative(self,root,mov):
        b=mov
        print('in')
        while root:
            if root.right==None and root.left==None:
                return b

            elif root.left!=None   and root.right!=None:
                print('both')

                b+=max(self.get_height_iterative(root.left,1),self.get_height_iterative(root.right,1))
                root=root.left
            elif root.left!=None  and root.right==None:
                print('left')
                root=root.left
                b+=1        
 
            elif root.right!=None   and root.left==None:
                root=root.right
                b+=1        



        return b
    def checkBalance_iterative(self,root,data):
        if root.left!=None and root.right==None:
            b=self.get_height_iterative(root.left,1) - self.get_height_iterative(root.right,0)
        elif root.right!=None and root.left==None:
                    b=self.get_height_iterative(root.left,0) - self.get_height_iterative(root.right,1)
        elif root.right!=None and root.left!=None:
                    b=self.get_height_iterative(root.left,1) - self.get_height_iterative(root.right,1)

        else:            
            b=self.get_height_iterative(root.left,0) - self.get_height_iterative(root.right,0)

        print(b,root.data,'bal','l')
        
        while b!=2 and b!=-2:
            if not root:
                break
            if root.left!=None and root.right==None:
                b=self.get_height_iterative(root.left,1) - self.get_height_iterative(root.right,0)
            elif root.right!=None and root.left==None:
                 b=self.get_height_iterative(root.left,0) - self.get_height_iterative(root.right,1)
            elif root.right!=None and root.left!=None:
                b=self.get_height_iterative(root.left,1) - self.get_height_iterative(root.right,1)

            else:            
                b=self.get_height_iterative(root.left,0) - self.get_height_iterative(root.right,0)
            print(b,root.data,'bal','w')

            if data>root.data:
                root=root.right
                print('right')
            elif root.data>data:
                print('left')
                root=root.left
            elif data==root.data:
                break
        if root!=None or root.data!=data:
            if b<-1 and data>root.right.data:
                print('LL',b)
                return self.leftRotationIterative(root)
            elif b>1 and data>root.left.data:
                print('RL',b)

                root.left=self.leftRotationIterative(root.left)
                return self.rightRotationIterative(root)
            elif b>1 and data<root.left.data:
                print('RR',b,data,root.data)

                return self.rightRotationIterative(root)
            elif b<-1 and data<root.right.data:
                print('LR',b)

                root.right=self.rightRotationIterative(root.right)
                return self.leftRotationIterative(root)
            
    def leftRotationIterative(self,root):
        z=root
        x=root.right
        y=x.left
        x.left=root
        root.right=y

        if z==self.root:self.root=x

        return x
    def rightRotationIterative(self,root):
        z=root
        x=root.left
        y=x.right
        x.right=root
        root.left=y

        if z==self.root:self.root=x
        return x

    #recursive
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
        return self.checkBalance(root,data)
    def checkBalance(self,root,data):
        balanceFactor=self.get_height(root.left)-self.get_height(root.right)
        print(balanceFactor,'bal')

        if balanceFactor<-1 and data > root.right.data:
            print('LL')

            return self.LeftRotation(root)

        if balanceFactor>1 and data > root.left.data:
            print('LR')

            root.left=self.LeftRotation(root.left)
            return self.RightRotation(root)   
        if balanceFactor>1 and data < root.left.data:
            print('RR')
            return self.RightRotation(root)
        if balanceFactor<-1 and data<root.right.data:
            print('RL')

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

        if z==self.root:
            self.root=x

        return x
    def RightRotation(self,root):
        z=root

        x=root.left
        y=x.right
        x.right=root
        root.left=y

        self.root=x
        
        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        x.height=1+max(self.get_height(x.left),self.get_height(x.right))
        if z==self.root:
            self.root=x

        return x
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

    # def get_balance_post_order(self,root):
    #     if root:
    #         a=self.get_height(root)
            
    #         if a==2:
    #             self.balance=a 

    #             x,y,z=root,root.left,root.left
    #             x.left=z.left
    #             x.right=z.right
    #             y.left=x
    #             y.right=z
    #             z.right=None
    #             z.left=None
    #             self.get_balance_post_order(root.left)
    #             self.root=y

    #             return y
    #         elif a==-2:
    #             self.balance=a 

    #             x,y,z=root,root.right,root.right
    #             x.left=z.left
    #             x.right=z.right
    #             y.left=x
    #             y.right=z
    #             x.right=None
    #             x.left=None
    #             self.get_balance_post_order(root.right)
    #             self.root=y
    #             return y
              
c=Tree()
while True:
    op=int(input('1.Add\n2.Display PreOrder\n3.Display InOrder\n4.Display PostOrder\n5.Exit\n'))
    if op==1:
        a=int(input('Data '))
        #c.root=c.insert(c.root,a)
        c.insert_iterative(a)
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
                

