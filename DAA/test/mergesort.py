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
def length(arr):
    c=0
    while arr:
        arr=arr.next
        c+=1
    return c
def dividelist(n,node):
    for i in range(n-1):
        node=node.next
    temp=node.next
    node.next=None
    return  temp

def mergesort(l,h):
    node=LinkedList()
    while l!=None and h!=None:
        if l.data>h.data:
            node.insert(h.data,node.head)
            h=h.next
        else:
            node.insert(l.data,node.head)
            l=l.next
    if l:
        while l:
            node.insert(l.data,node.head)
            l=l.next
    if h:
        while h:
            node.insert(h.data,node.head)
            h=h.next
    return node.head
def divide(node):
    p=length(node)
    if p>1:
        mid=p//2
        midpoint=dividelist(mid,node)
        left=divide(node)
        right=divide(midpoint)
        return mergesort(left,right)
    return node
def iterate(node,n):
    for i in range(n-1): 
        if not node:
            return None

        node=node.next
    return node
def binarysearch(l,h,node,x):
    print(l,h)
    if l<h:
        mid=l+(h-l)//2
        midpoint=iterate(node,mid)
        if not midpoint:
            return "Not Found"
        if midpoint.data==x:
            return 'Found'
        elif x<midpoint.data:
           return  binarysearch(l,mid-1,node,x)
        else:
           return binarysearch(mid+1,h,midpoint,x)
    return 'not found'
l=LinkedList()
x=[1,12,3,3,45,56,6]
for i in x:
    l.insert(i,l.head)
l.display(l.head)
x=divide(l.head)
l.head=x
l.display(l.head)
print(binarysearch(0,length(l.head),l.head,112))