class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data,node):
        if node==None:
            self.head=Node(data)
        else:
            while node.next!=None:node=node.next
            node.next=Node(data)
        

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
def insertionSort(head):
    temp=head
    sorted=None
    while temp:
        next=temp.next
        sorted=sort(sorted,temp)
        temp=next
    head=sorted
    return sorted
def sort(head,node):
    if head==None or head.data>node.data:
        node.next=head
        head=node
    else:
        cur=head
        while cur.next  and cur.next.data<node.data:
            cur=cur.next

        node.next=cur.next
        cur.next=node
    return head
def iterate(arr,n):
    for i in range(n):
        arr=arr.next

    return arr
def binarysearch(l,h,arr,f):
    if  l<=h:
        mid=l+(h-l)//2
        p=iterate(arr,mid)
        print(p.data,mid)
        if p.data==f:
            return True
        elif f<p.data:
            return  binarysearch(l,mid-1,arr,f)

        else:
           return binarysearch(mid+1,h,arr,f)
    else:
       return False

p=[1,12,56,3,3,45,]
l=LinkedList()
for i in p:
    l.insert(i,l.head)
l.display(l.head)
print("Sorting")
l.head=insertionSort(l.head)
l.display(l.head)
print(binarysearch(0,length(l.head),l.head,45))