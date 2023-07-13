class Queue:
    def __init__(self,ln):
        self.l=ln
        self.q=[]
    def insert(self,data):
        if(len(self.q)<self.l):
            self.q.append(data)
            return 'added'
        else:
            return 'isFull'
    def delete(self):
        try:
            self.q.pop(0)
        except IndexError:
            print('Queue Underflow')
    def isEmpty(self):
        if(len(self.q)==0): return f'Empty available space is {self.l-len(self.q)}'
        else:return  f'Not Empty  available space is {self.l-len(self.q)} '
    def isfull(self):

        if(len(self.q)>=self.l):return 'Full'
        return 'Not full'
    def Display(self):
        print(self.q)
    def search(self,data):
        o=self.q
        for i in range(len(o)):
            if o[i]==data:
                print(i)
        try:
            return self.q.index(data)
        except:
            return 'Not There'

s=Queue(10)
while True:
    op=int(input('1.Initialize\n2.Add\n3.Delete\n4.isEmpty\n5.isfull\n6.Display\n7.search\n8.Exit\n'))
    if op==1:
        n=int(input('Enter length of queue '))
        s=Queue(n)
    elif op==2:
        n=int(input('Enter number '))

        print(s.insert(n))
    elif op==3:
        s.delete()
    elif op==4:
        print(s.isEmpty())
    elif op==5:
        print(s.isfull())
    elif op==6:
        s.Display()
    elif op==7:
        n=int(input('enter the value you want to search ')) 
        print(f"position: {s.search(n)}")
    elif op==8:break