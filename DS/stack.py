
class Stack:
    l=[]
    min=0
    def insert(self,a):
        s=self.l
        s.append(a)
        self.min=a
        self.l=s
    def Pop(self):
        if(len(self.l)>0):
            s=self.l
            s.pop()
            if(len(self.l)==0):
                self.min=-1
            else:   
                self.min=s[-1]
            self.l=s
        else:
            print('Stack Underflow')
    def peek(self):
        a=self.l
        print(a[-1])
    def view_stack(self):
        print(self.l)
    def getMinimum(self):
        a=self.l
        b=list(a)
        o=self.min
        if(o!=-1):
            for i in range(len(b)):
                p=b.pop()
                if(p<o and  o!=-1):
                    o=p
        self.min=o
        print(o,'min')

s=Stack()
s.insert(17)
s.insert(7)
s.insert(3)
s.insert(15)
s.insert(10)
s.insert(2)
s.insert(1)
s.getMinimum()
s.Pop()
s.getMinimum()
s.Pop()
s.Pop()
s.getMinimum()
s.Pop()
s.Pop()
s.Pop()
s.Pop()
s.Pop()
s.getMinimum()
