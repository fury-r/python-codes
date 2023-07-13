



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
        self.flag=0
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
                    tmp.right=Node(data)
                    break
                elif data<tmp.data and tmp.left==None:

                    tmp.left=Node(data)
                    if c>self.level:self.level=c
                    break
                elif data>tmp.data  and tmp.right!=None: 

                    tmp=tmp.right
                    if c>self.level:self.level=c

                elif data<tmp.data and tmp.left!=None:

                    tmp=tmp.left

                else:
                    break
                
        self.checkBalance_iterative(self.root,data)
        self.flag=0
    def  get_height_iterative(self,root,mov):
        b=mov
        while root:
            if root.right==None and root.left==None:
                return b

            elif root.left!=None   and root.right!=None:
                #print('both',root.left,root.data,root.right)

                b+=max(self.get_height_iterative(root.left,1),self.get_height_iterative(root.right,1))
                root=root.left
            elif root.left!=None  and root.right==None:
                #print('left',root.left,root.data,root.right)
                root=root.left
                b+=1        
 
            elif root.right!=None   and root.left==None:
               # print('right',root.left,root.data,root.right)

                root=root.right
                b+=1        


        return b
    def checkBalance_iterative(self,root,data):
        if root:
            if(root.data==7 and root.left):
                print(root.left.data,'left of 7 before')
            if data>root.data:
                self.checkBalance_iterative(root.right,data)
            elif root.data>data:

                self.checkBalance_iterative(root.left,data)

            
            prev=None
            if(root.data==7 and root.left):
                print(root.left.data,'left of 7')
            b=0
            if not root:
                return
            if root.left!=None and root.right==None:
                b=self.get_height_iterative(root.left,1) - self.get_height_iterative(root.right,0)
            elif root.right!=None and root.left==None:
                b=self.get_height_iterative(root.left,0) - self.get_height_iterative(root.right,1)
            elif root.right!=None and root.left!=None:
                b=self.get_height_iterative(root.left,1) - self.get_height_iterative(root.right,1)

            else:            
                b=self.get_height_iterative(root.left,0) - self.get_height_iterative(root.right,0)
            print(b,'balance at',root.data,'---------------------')

            print(prev,'--------------------',b,root,data)
            root= root if not prev else prev
            if root!=None and root.data!=data:
                
                if root.left :
                    print('-----------------------in',root.left.data,root.data)
                if b<-1 and data>root.right.data  and self.flag==0:
                    parent= self.get_parent(self.root,root) if self.root!=root else 0

                    print('LL balance',b,root.data,data,'getparent----------------------------')
                    x=self.leftRotationIterative(root)
                    #(f'---------------------------\nparent {parent.data}\nreturned {x.data},{x.left.data},{x.right.data},\n----------------------------------')

                    if x!=self.root:
                        if x.data<parent.data:parent.left=x
                        else:parent.right=x
                elif b>1 and data>root.left.data  and self.flag==0:
                    print('LR balance',b,data,'getparent----------------------------unbalance at',root.data)
                    parent= self.get_parent(self.root,root) if self.root!=root else 0

                    root.left=self.leftRotationIterative(root.left)
                    x=self.rightRotationIterative(root)
                    #print(f'parent {parent.data}\nreturned {x.data}\n----------------------------------')

                    if x!=self.root:
                        if x.data<parent.data:parent.left=x
                        else:parent.right=x
                elif b>1 and data<root.left.data  and self.flag==0:
                    parent=self.get_parent(self.root,root)

                    print('RR balance',b,root.data,data,'getparent----------------------------')
                    x=self.rightRotationIterative(root)
                    #print(f'---------------------------\nparent {parent.data}\nreturned {x.data},{x.left.data},{x.right.data},\n----------------------------------')
                    if x!=self.root:
                        if x.data<parent.data:parent.left=x
                        else:parent.right=x
                elif b<-1 and data<root.right.data  and self.flag==0:
                    print('RL balance',b,root.data,data,'getparent----------------------------')
                    
                    parent= self.get_parent(self.root,root) if self.root!=root else 0

                    root.right=self.rightRotationIterative(root.right)
                    x=self.leftRotationIterative(root)
                    #print(f'---------------------------\nparent {parent.data}\nparents child {parent.left.data}\nreturned {x.data},{x.left.data},{x.right.data},\n----------------------------------')

                    if x!=self.root:
                        if x.data>parent.data:parent.right=x
                        else:parent.left=x
                    #print(f'---------------------------\nparent {parent.data}\nparents child {parent.left.data}\nreturned {x.data},{x.left.data},{x.right.data},\n----------------------------------')
             
    def leftRotationIterative(self,root):
        z=root
        x=root.right
        y=x.left
        x.left=root
        root.right=y

        if z==self.root:self.root=x
        self.flag=1
        return x
    def rightRotationIterative(self,root):
        z=root
        x=root.left
        y=x.right
        x.right=root
        root.left=y
        self.flag=1

        if z==self.root:self.root=x
        print(x.data,'returned-----')
        return x
    def get_node(self,root,a):
        if root.left==a or root.right==a:
            return root
        elif root  and a.data>root.data:
            return self.get_node(root.right,a)
        elif root  and a.data<root.data:

            return self.get_node(root.left,a)
#-----------------------------------------------------------------------------------------------------------------------------------
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
    def get_parent(self,root,dest):
        if root:
            if dest.data>root.data and root.right==dest:
                return  root
            elif dest.data<root.data and root.left==dest:
                return  root
            elif dest.data>root.data:
                return self.get_parent(root.right,dest)
            elif dest.data<root.data:
                return self.get_parent(root.left,dest)
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
    def PreOrder(self,root,a):
        if root:
            print(root.data,a)

            self.PreOrder(root.left,'left')

            self.PreOrder(root.right,'right')

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

        c.PreOrder(c.root,'root')
    elif op==3:
        print('Inorder\n')

        c.Inorder(c.root)
    elif op==4:
        print('Postorder\n')

        c.PostOrder(c.root)
    elif op==5:
        break
                

