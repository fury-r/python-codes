class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Linkedlist:
    def __init__(self) :
        self.head=None
    def insert(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return 1
        temp=self.head
        while temp.next!=None:temp=temp.next
        new.prev=temp
        temp.next=new   
        return 1
    def display(self):
        temp,l=self.head,[]
        while temp:
            l.append(temp.data)
            temp=temp.next
        print(l)
    def length(self):
        i=0
        temp=self.head
        while temp:
            temp=temp.next
            i+=1
        return i
#iterating to a certain position
def iterate(arr,n):
    temp=arr
    while n>0 and temp.next:
        temp=temp.next
        n-=1
    return temp
def display(head):
    temp=head
    if temp.prev:
        while temp.prev!=None:   
            temp=temp.prev
    l=[]
    while temp:
        l.append(temp.data)
        temp=temp.next
    print(l)
#going back to head
def switchtohead(arr):
    while arr.prev:
        arr=arr.prev
    return arr
def quicksort(arr,l,h):
    if l<h:
        arr=switchtohead(arr)
        #headpointer
        head=iterate(arr,l)
        #tailpointer
        tail=iterate(arr,h)
        mid=partition(l,h,head,tail)
        quicksort(arr,mid+1,h)
        quicksort(arr,l,mid-1)
        return arr
def partition(l,h,head,tail):
    pivot=head
    display(head)
    print(head.data,tail.data)
    while l<h:  
        while l<h and head.data<=pivot.data:
            l+=1
            head=head.next
        while h>=l and  tail.data>=pivot.data:
            h-=1
            tail=tail.prev
        if l<h:
            head.data,tail.data=tail.data,head.data
            
            display(head)
    if tail and pivot:
        pivot.data,tail.data=tail.data,pivot.data

    display(pivot)
    return h
            
l=Linkedlist()
x=[1,12,3,3,45,56,6,0,0]
for i in x:
    l.insert(i)
l.display()
o=quicksort(l.head,0,l.length()-1)
o=switchtohead(o)
l.head=o
print('Result')
l.display()