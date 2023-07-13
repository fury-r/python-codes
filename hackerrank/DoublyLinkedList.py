class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinklist:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,data):
        n=Node(data)
        if(self.head==None):
            self.head=n
            self.tail=n
        else:
            tmp=self.tail
            tmp.next=n
            n.prev=tmp
            self.tail=n
    def display(self):
        tmp=self.head
        while tmp!=None:
            print(tmp.data)
            tmp=tmp.next
def sortedInsert(llist, d):
    tmp1,tmp2=llist,llist.next
    n=Node(d)
    while tmp2.next!=None:
        if tmp2.data>d:
            break
        tmp1=tmp2
        tmp2=tmp2.next

    if(tmp1.data>d):
        n.next=tmp1
        tmp1.prev=n
        llist.head=n
        return n
    elif(tmp2.next==None and tmp2.data<d):
        tmp2.next=n
        n.prev=tmp2
        return llist
    tmp1.next=n
    n.prev=tmp1
    n.next=tmp2
    tmp2.prev=n
    return llist
def reverse(llist):


    while llist.head.next!=None:
        tmp1=tmp2=llist.head
        while tmp2.next!=None:
            tmp1=tmp2
            tmp2=tmp2.next


        tmp=tmp2.next
        tmp2.next=tmp1
        tmp2.prev=tmp
        tmp1.next=tmp
    tmp=llist.head
    llist.head=llist.tail
    llist.tail=tmp

l=DoublyLinklist()
l.insert(2)
l.insert(3)
reverse(l)
l.display()
sortedInsert(l.head,1)
