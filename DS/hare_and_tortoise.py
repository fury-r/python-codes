class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        n=Node(data)
        h=self.head
        if(self.head==None):
            self.head=n
        else:
            while h.next!=None:
                h=h.next
            h.next=n

    def loop_insert(self,data,to):
        h=self.head
        tmp=self.head
        while h.next!=None:
            if(h.data==to):
                break
            h=h.next
        while tmp.next!=None:
            tmp=tmp.next
        n=Node(data)
        tmp.next=n
        tmp=tmp.next
        tmp.next=h
    def display(self):
        tmp=self.head
        while tmp.next!=None:
            print(tmp.data)
            tmp=tmp.next
        print(tmp.data)
    def detect_loop(self):
        s=f=self.head
        i=0
        while True:
            i+=1
            s=s.next
            f=f.next.next
            if(f.next==s.next):
                return s.next
    def detect_start_and_break(self,meet):
        start=temp=self.head
        while start.next!=meet:
            temp=meet
            start=start.next
            meet=meet.next
        temp.next=None
        return meet
l=linklist()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)
l.loop_insert(7,3)

a=l.detect_loop()
l.detect_start_and_break(a)
l.display()

