




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
def switchtohead(arr):
    while arr.prev:
        arr=arr.prev
    return arr
def iterate(arr,n):
    for i in range(n):
        arr=arr.next

    return arr
def length(p):
    c=0
    while p:
        c+=1
        p=p.next
    return c
def quicksort(l,h,arr):
    if l<h:
        x=iterate(arr,l)
        y=iterate(arr,h)
        p=partition(l,h,x,y)
        quicksort(l,p-1,arr)
        quicksort(p+1,h,arr)
def partition(l,h,head,tail):
    pivot=head
    while l<h:
        print('sdfg',l,h,pivot.data,head.data,tail.data)
        while l<h and pivot.data<=head.data:
            l+=1
            head=head.next
        while  pivot.data>tail.data:
            h-=1
            tail=tail.prev
        if l<h:
            tail.data,head.data=head.data,tail.data
    pivot.data,tail.data=tail.data,pivot.data
    return h
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
x=quicksort(0,length(l.head)-1,l.head)
l.display(l.head)
print(linearSearch(l.head,5))