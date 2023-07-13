

class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

class Tree:
    def __init__(self):
        self.root=None
        self.level=None
        self.count=0
    def insert(self,data):
        n=Node(data)
        if self.root==None:
            self.root=n
        else:
            tmp=self.root

            while True:
                if tmp.data==n.data:return 'It already exists!!!!'
                if n.data>tmp.data and tmp.right==None:
                    print('in right')
                    tmp.right=n
                    self.count=self.count+1
                    break
                elif n.data<tmp.data and tmp.left==None:
                    print('in left')
                    tmp.left=n
                    self.count=self.count+1

                    break
                elif n.data>tmp.data  and tmp.right!=None:
                    print('in right')

                    tmp=tmp.right
                elif n.data<tmp.data and tmp.left!=None:
                    print('in left')
 
                    tmp=tmp.left
                else:
                    break
    def recursive_insert(self,root,data):
        if not self.root:
            self.root=Node(data)
        elif not root:
            return Node(data)
        elif data>root.data:
            root.right=self.recursive_insert(root.right,data)
        elif data<root.data:
            root.left=self.recursive_insert(root.left,data)
    def PreOrder(self,root,pos):
          if root:           
            print(root.data,pos)

            self.PreOrder(root.left,'left')
            self.PreOrder(root.right,'right')
    def PostOrder(self,root,pos):
        if root:
            
            self.PostOrder(root.left,'left')
            self.PostOrder(root.right,'right')
            print(root.data,pos)

    def InOrder(self,root,pos):
        if root:
            self.InOrder(root.left,'left')
            print(root.data,pos)
            self.InOrder(root.right,'right')
            
              
c=Tree()
while True:
    op=int(input('1.Add\n2.Display PreOrder\n3.Display InOrder\n4.Display PostOrder\n5.Exit\n'))
    if op==1:
        a=int(input('Data '))
        print(c.insert(a))
        #c.recursive_insert(c.root,a)
        print(c.root.left,c.root.right)
    elif op==2:
        print('Preorder\n')

        c.PreOrder(c.root,'root')
    elif op==3:
        print('Inorder\n')

        c.InOrder(c.root,'root')
    elif op==4:
        print('Postorder\n')

        c.PostOrder(c.root,'root')
    elif op==5:
        break
                

