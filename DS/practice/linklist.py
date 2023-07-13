class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinklist:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        if not self.head:
            self.head=Node(data)
        else:
            tmp=self.head
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=Node(data)
            return Node(data)
    def loop_insert(self,n,con):
        tmp=self.head
        for i in range(0,n-1):
            tmp=tmp.next

        con.next=tmp
    def detect_loop(self):
        i=set()
        tmp=self.head
        while tmp.next!=None:
            if tmp in i:
                return 'Loop'
            i.add(tmp)
            tmp=tmp.next

        return 'No loop'
    def break_loop(self):
        i=set()
        meet=tmp=self.head
        while tmp not in i:
            i.add(tmp)

            if tmp.next==None:
                break
            meet=tmp
            tmp=tmp.next
        print(meet.next)
        meet.next.next=None
    def display(self,root):
        if root:
            print(root.data)
            self.display(root.next)
    def reverse(self):
        tail=self.head
        while tail.next!=None:
            tail=tail.next
        
        while self.head.next!=None:
            tmp=tmp1=self.head
            while tmp1.next!=None:
                tmp=tmp1
                tmp1=tmp1.next
            tmp.next=tmp1.next
            tmp1.next=tmp
        self.head=tail
l=SinglyLinklist()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(5)
l.display(l.head)

a=l.insert(6)
l.loop_insert(5,a)


print(l.detect_loop())
l.break_loop()
print(l.detect_loop())
l.reverse()
l.display(l.head)
l.reverse()

l.display(l.head)
