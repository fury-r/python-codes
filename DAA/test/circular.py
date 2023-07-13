


global k
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
            self.head.next=self.head
            self.head.prev=self.head
            return 1
        temp=self.head
        while temp.next!=self.head:temp=temp.next
        new.prev=temp
        temp.next=new  
        new.next=self.head
        self.head.prev=new 
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
        p=set()
        while temp not in p:
            p.add(temp)
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
    l=[]
    o=set()
    while temp  not in o:

        o.add(temp)

        l.append(temp.data)
        temp=temp.next
    print(l)
def displayloop(head):
    temp=head
    l=[]
    o=set()
    while temp :

        o.add(temp)

        print(temp.data)
        temp=temp.next
    print(l)
#going back to head
def switchtohead(arr):
    print(k.data)
    return k

def quicksort(arr,l,h,a):
    if l<h:
        arr=a
        #headpointer
        head=iterate(arr,l)
        #tailpointer
        tail=iterate(arr,h)
        mid=partition(l,h,head,tail,a)
        quicksort(arr,mid+1,h,a)
        quicksort(arr,l,mid-1,a)
        return arr
def partition(l,h,head,tail,a):
    pivot=head
    print(head.data,tail.data)
    while l<h:  
        while l<h and head.data<=pivot.data:
            l+=1
            head=head.next
        while h>=l and  tail.data>=pivot.data and tail!=a :
            h-=1
            tail=tail.prev
        if l<h:
            head.data,tail.data=tail.data,head.data
            
    if tail and pivot:
        pivot.data,tail.data=tail.data,pivot.data

    return h
            
l=Linkedlist()
k=l.head
x=[1,12,3,3,45,56,6,0,0]
for i in x:
    l.insert(i)
#l.display()
display(l.head)
# l.head.prev.next=None
# l.head.prev=None
quicksort(l.head,0,l.length(),l.head)
p=iterate(l.head,l.length()-1)
p.next=l.head
l.head.prev=p
display(l.head)
displayloop(l.head)
