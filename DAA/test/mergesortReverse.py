class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            node=Node(data)
            temp.next=node
            node.prev=temp

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
def mergesort(left,right):
    l=LinkedList()
    while left and right:
        if left.data>right.data:
            l.insert(left.data)
            left=left.next
        else:
            l.insert(right.data)
            right=right.next

    while right:
        l.insert(right.data)
        right=right.next
    while left:
        l.insert(left.data)
        left=left.next
    return l.head
def dividelist(node,mid):
    x=None
    for i in range(mid):
        x=node
        node=node.next
    x.next=None
    return node
def divide(arr):
    p=length(arr)
    print(p,'sdfsdf')
    if p>1:
        mid=p//2
        midpoint=dividelist(arr,mid)
        left=divide(arr)
        right=divide(midpoint)
        return mergesort(left,right)
    else:
        return arr
        
def iterate(node,n):
    for i in range(n-1): 
        if not node:
            return None

        node=node.next
    return node
def binarysearch(l,h,node,x):
    print(l,h)
    if l<=h:
        mid=l+(h-l)//2
        midpoint=iterate(node,mid)
        if midpoint.data==x:
            return "Found"
        elif midpoint.data>x:
                        return binarysearch(mid+1,h,node,x)

        else:
                        return binarysearch(l,mid-1,node,x)

    return "Not found"
l=LinkedList()
x=[1,12,3,3,45,56,6]

for i in x:
    l.insert(i)
l.display(l.head)
print('---------------')
l.display(l.head)
x=divide(l.head)
l.head=x
l.display(l.head)
print(binarysearch(0,length(l.head),l.head,56))