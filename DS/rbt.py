

class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
        self.height=1
        self.color='R'

class Tree:
    def __init__(self):
        self.root=None
        self.level=0
        self.flagroot=None
        self.set=set()
        self.l=[]
        self.flag=0
        self.parent=0
        self.color=None
    def insert(self,root,data):
        if self.root==None:
            self.root=Node(data)
            self.root.color='B'
        elif not root:
            return Node(data)
        elif root.data==data:
            return None
        elif root.data>data:

            a=self.insert(root.left,data)
       
            if root.data==self.flagroot:
                return a
            if  self.flag==0 and a:
                print(' not flag\n-------\n ',a.data,root.data,self.flagroot)

                root.left=a
                
        elif root.data<data:
            a=self.insert(root.right,data)
                
            if root.data==self.flagroot:
                root.right=None
                return a
            if  self.flag==0 and a:
                print(' not flag\n-------\n ',a.data,root.data,self.flagroot)
                root.right=a
        if self.flag==0:
            if root and root.color!='B':
                parent=0
                self.traverse+=1
                if root.right:print(root.data,data,'---------------',root.right.data,root.left)
                if root.color=='R' and data>root.data and root.right.color=='R' or root.color=='R' and data<root.data and root.left.color=='R':
                    print('search',root.data)
                    parent=self.get_parent(self.root,root)
                    print('in RR conflict',parent)
                    self.detectrotation(parent,data,[])
                    if (parent.data<root.data  and parent.left==None) or ( parent.data>data   and   parent.right==None):
                        return self.rotation(parent,self.l)
                    elif (parent.data<root.data  and parent.right.color=='B') or ( parent.data>data   and   parent.left.color=='B'):
        
                        return self.rotation(parent,self.l)
                    elif (parent.data<root.data and parent.right.color=='R') or (parent.data>root.data and  parent.left.color=='R'):
                        print('in recolor',parent.data)
                        if data>self.root.data:
                                return self.recolor(self.root.right,data)
                        else:
                                return self.recolor(self.root.left,data)

    def detectrotation(self,root,data,l):
        if  root:
            if data>root.data:
                self.l.append('R')
                self.detectrotation(root.right,data,l)
            elif data<root.data:
                self.l.append('L')


                self.detectrotation(root.left,data,l)
         

    def recolor(self,root,data):
        if not root:
            return root
        else:
            self.recolor(root.left,data)
             
            self.recolor(root.right,data)
        parent=0
        if root.data != data :
                if self.color:
                    print(root.color,self.color,'Recolor RR')

                    if (root.color=='R' and self.color.color=='R') and ((root.data>data and root.left==self.color) or (root.data<data and root.right==self.color)) :
                        parent=self.get_parent(self.root,root)
                        print('in\n----------------',self.color.data,parent.data,root.data,parent.right.color,parent.left.color,parent.right.data,parent.left.data,parent.color,root.color)
                        self.detectrotation(self.root,root.data,[])
                        print(self.l,'rotation',root.color)
                        if (parent.data<root.data  and parent.left==None) or ( parent.data>data   and   parent.right==None) or(parent.data<root.data  and parent.left.color=='B') or ( parent.data>data   and   parent.right.color=='B'):
                            grandparent=self.get_parent(self.root,parent)

                            return self.rotation(parent,self.l)
                parent=self.get_parent(self.root,root)

                print('in recolor-----------------------------',parent.data,root.data,root.color)
                if root.color=='B' and self.root != root:

                    root.color='R'
                elif root.color=='R' and self.root != root:

                    root.color='B'
                if   self.parent==0:
                    if (root.data<parent.data and parent.right.color=='B' and self.root != root) :
                        print(1)
                        parent.left.color='R'

                    elif  (root.data<parent.data   and parent.right.color=='R' and self.root != root):
                        parent.right.color='B'
                        print(4)
                    if parent.left!=root and parent.left!=None:
                        if  (root.data>parent.data and parent.left.color=='B' and self.root != root):
                                parent.left.color='R'
                                print(2)

                        elif (root.data>parent.data  and parent.left.color=='R' and self.root != root ) :
                            parent.left.color='B'
                        print(3)
                    self.parent+=1
 
                self.color=root
                

    def rotation(self,root,l):
        rot=''
        if len(l)>=2:
            rot=l[-2]+l[-1]
        else:
            rot=l[-1]
        print(rot,'rot',root.data,'\n------------')
        if  rot=='RR':
            print('in L')
            x= self.leftRotation(root)
            return self.rootcolor(x)
        elif rot=='LR':
            print('in LR',root.data)
            root.left=self.leftRotation(root.left)
            x= self.rightRotation(root)
            return self.rootcolor(x)

        elif rot=='LL' :
            print('in R')
            x= self.rightRotation(root)
            return self.rootcolor(x)

        elif rot=='RL':
            print('in RL')
            root.right=self.rightRotation(root.right)
            x= self.leftRotation(root)
            return self.rootcolor(x)

    def rootcolor(self,root):
        root.color=='B'
        root.right.color='R'
        root.left.color='R'
        return root
    def leftRotation(self,root):
        print(root.data,'in LL')
        if root.data==10:
            print(root.right.left.data,'-----------------------ffd')
        z=root
        x=root.right
        y=x.left
        x.left=root
        if y:print(y.data,'-----')
        root.right=y

        self.flagroot=root.data
        print(self.flagroot,'flag')
        if z==self.root:
            print('Flag\n-------------',x.data)

            self.root=x
            self.flag=1


        if x.right :
            x.right.color=='R'
        if x.left:
            x.left.color='R'

        x.color='B'
        if self.root.data==16:
            print(self.root.left.right.data,'-----------------------fghjhjfd')
        print('return',x.data,self.flagroot)
        return x
    def rightRotation(self,root):
        print(root.data,'in RR')
        z=root
        x=root.left
        y=x.right
        x.right=root
        root.left=y
        print(self.flagroot,'flag')

        self.flagroot=root.data

        if z==self.root:
            print('Flag\n-------------',x.data)
            self.root=x
            self.flag=1

        if x.right!=None :
            print('in')
            x.right.color=='R'
        if x.left!=None:
            x.left.color='R'
        x.color='B'
        print('return',x.data,self.flagroot)

        return x     

    def get_parent(self,root,search):
        if root:
            if root.right!=None and  root.right==search :
                return root
            elif root.left!=None and root.left==search:
                return root
            elif search.data>root.data :
                print('L')
                return self.get_parent(root.right,search)
            elif search.data<root.data:
                print('R')
                return self.get_parent(root.left,search)




    def get_grandFather(self,root,search):
      if root:
            if root.right!=None:
                if  root.right.data==search.data:
                    return root
            if root.left!=None:
                if root.left.data==search.data:
                    return root
            elif root.data>search.data :
                return self.get_grandFather(root.left,search.data)
            elif root.data<search.data:
               return self.get_grandFather(root.right,search.data)
    def PreOrder(self,root,a):
        if root:
            print(f'{root.data} color:{root.color} position: {a}')
            self.PreOrder(root.left,'left')
            self.PreOrder(root.right,'right')   
c=Tree()
while True:
    op=int(input('1.Add\n2.Display PreOrder\n3.Display InOrder\n4.Display PostOrder\n5.Exit\n'))
    if op==1:
        c.traverse=0
        a=int(input('Data '))
        c.flag=0
        c.flagroot=0
        c.color=None
        z=c.insert(c.root,a)
        print(c.root.left,c.root,c.root.right,'pos')

    elif op==2:
        print('Preorder\n')
        x=c.root
    

        c.PreOrder(c.root,'root')

    elif op==3:
        print('Inorder\n')

        c.Inorder(c.root)
    elif op==4:
        print('Postorder\n')

        c.PostOrder(c.root)
    elif op==5:
        break
                


