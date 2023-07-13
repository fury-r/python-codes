
class Stack:
    l=[]
    min=None
    def insert(self,a):
        if(len(self.l) ==0 ):
            s=self.l
            s.append(a)
            self.min=a
        elif(a<self.min):
            t=(2*a)-self.min
            s=self.l
            s.append(t)
            self.min=a
        else:
            s=self.l
            s.append(a)
    def Pop(self):
        stack=self.l
        if(len(stack)==0):
            print("Stack Underflow")
        else:
            q=stack.pop()
            if(q<self.min):
                self.min=(2*self.min)-q
    def peek(self):
        a=self.l
        print(a[-1])
    def view_stack(self):
        print(self.l)
    def getMinimum(self):
        if(len(self.l)!=0):
            print(self.min)
        else:
            print(-1)

s=Stack()
s.insert(17)
s.insert(7)
s.insert(3)
s.insert(15)
s.insert(10)
s.insert(2)
s.insert(1)
s.getMinimum()
s.getMinimum()

s.getMinimum()

