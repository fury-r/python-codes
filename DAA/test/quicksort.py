


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data,node):
        if node==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            temp=Node(data)
            temp.prev=self.tail
            self.tail.next=temp
            self.tail=temp
    def display(self,node):
        if node:
            print(node.data)
            self.display(node.next)

def quicksort(l,h):
    if h!=None and l!=h and l!=h.next:
        temp=partition(l,h)
        quicksort(l,temp.prev)
        quicksort(temp.next,h)
def switchtohead(arr):
    while arr.prev:
        arr=arr.prev
    return arr
def partition(l,h):
    pivot=h.data
    i=l.prev
    j=l
    while (j!=h):
        if (j.data<=pivot):
            i=l if not i else i.next;
            temp=i.data;
            i.data=j.data;
            j.data=temp;
        j=j.next
    i=l if not i else i.next
    temp=i.data
    i.data=h.data
    h.data=temp
    return i
def linearSearch(node,x):
    
    while node!=None and node.data!=x:
        node=node.next
    if node:
        return 'Found'
    return 'Not found'
p=[1,12,3,45,56,3,3,3,1,5.0]
l=LinkedList()
for i in p:
    l.insert(i,l.head)
x=quicksort(l.head,l.tail)
l.display(l.head)
print(linearSearch(l.head,11))