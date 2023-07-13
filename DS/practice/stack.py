class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None

class Stack:
    def __init__(self):
        self.root=None
        self.min=None
    def push(self,data):
        if not self.root:
            self.root=Node(data)
            self.min=data
            return 0
        elif data<self.min:
            temp=(2*data)-self.min
            self.min=data
            n=Node(temp)
            n.prev=self.root
            self.root=n
        else:
            n=Node(data)
            n.prev=self.root
            self.root=n
    def pop(self):
        if self.root:
            root=self.root
            self.root=self.root.prev
            if root.data<self.min:
                self.min=(2*self.min)-root.data

    def getMinimum(self):
        print(self.min)
s=Stack()

s.push(17)

s.push(7)
s.push(3)
s.push(15)
s.push(10)
s.push(2)
s.push(1)
s.getMinimum()
s.pop()
s.getMinimum()
s.pop()

s.pop()

s.getMinimum()
