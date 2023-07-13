

class Node:
    def __init__(self,data):
        self.addr=None
        self.data=data

class QeueuLinklist:
    def __init__(self,l):
        self.n=l
        self.head=self.tail=None
        self.current_length=0
    def insert(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            self.tail=node
            self.current_length=self.current_length+1
            return 'Done'

        elif self.current_length<self.n:
            self.tail.addr=node
            self.tail=node
            self.current_length=self.current_length+1
            return 'Done'
        else:
            return 'Queue Full'
    def delete(self):
        if self.current_length!=0:
            tmp=self.head
            self.head=tmp.addr
            tmp.addr=None
            self.current_length=self.current_length-1
        else:print('isEmpty')
    def isFull(self):
        if self.n==self.current_length: return 'isFull'
        else:return 'NotFull'
    def isEmpty(self):
        if self.current_length==0:return 'isEmpty'
        else:return 'NotEmpty'
    def display(self):
        tmp=self.head
        n=''
        while tmp!=None:
            n=n+str(tmp.data)+','
            tmp=tmp.addr
        print(n)
    def search(self,data):
        if self.current_length!=0:

            tmp=self.head
            n=0
            while tmp!=None:
                if tmp.data==data:
                    print(f"position: {n}")
                    return 0
                tmp=tmp.addr
                n+=1
            print('Not there')
        else:print('isEmpty')

s=QeueuLinklist(10)
while True:
    op=int(input('1.Initialize\n2.Add\n3.Delete\n4.isEmpty\n5.isfull\n6.Display\n7.search\n8.Exit\n'))
    if op==1:
        n=int(input('Enter length of queue '))
        s=QeueuLinklist(n)
    elif op==2:
        n=int(input('Enter data '))

        print(s.insert(n))
    elif op==3:
        s.delete()
    elif op==4:
        print(s.isEmpty())
    elif op==5:
        print(s.isFull())
    elif op==6:
        s.display()
    elif op==7:
        n=int(input('enter the value you want to search '))
        s.search(n) 
    elif op==8:break