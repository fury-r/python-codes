

import queue


class  Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
        self.code=''
    def insert(self,string):
        queue=[[i,string.count(i)] for i in set(string)]
        queue=sorted(queue,key=lambda item:item[1],reverse=True)
        l=list(queue)
        before=sum([ i[1] for i in queue])*8
        while len(queue)>1:
            x,y=queue.pop(),queue.pop()
            sumxy=x[1]+y[1]
            if not self.root:
                self.root=Node(sumxy)
                self.root.right=Node(y[0])
                self.root.left=Node(x[0])
            else:
                main=Node(sumxy)
                main.left=Node(y[0])
                main.right=self.root
                self.root=main
            queue.append([sumxy,sumxy])
        print(f"{before}--------------------------")
        code={}
        after=len(l)*8
        for i in l:
            self.getCode(self.root,i[0],'')
            code[i[0]]={
                'code':self.code,
                'freq':i[1],
                'length':len(self.code)*i[1]
            }
            after+=i[1]+code[i[0]]['length']
            self.code=''
        print(f"{after}-------------------")
        print(code)
    def getCode(self,root,data,p):
        if root.data==data:
            self.code=p
        if root.right:self.getCode(root.right,data,p+"1")
        if root.left:self.getCode(root.left,data,p+'0')
    def decode(self,s):
        p=''
        temp=self.root
        for  i in s:
            if temp.right==None and i=='1' or temp.left==None and i=='0':
                p+=temp.data
                temp=self.root
            if temp.right and i=='1':
                temp=temp.right
            elif temp.left and i=='0':
                temp=temp.left
        p+=temp.data
        print(p)
        return p
l=Tree()
#x='asdasdasdasa'
f=open("./t.txt",'r')
x=f.read()
f.close()
f=open("./t.txt",'a')
l.insert(x)
p='010110'

f.write(l.decode(p))
