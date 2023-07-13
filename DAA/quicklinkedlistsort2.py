


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
def iterate(arr,n):
    temp=arr
    print(n)
    for i in range(n-1):
        temp=temp.next
    return temp
def reverse(head):
    temp=head
    if temp.next:
        while temp.next!=None:   
            temp=temp.next
    l=[]
    while temp:
        l.append(temp.data)
        temp=temp.prev

    print(l)
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
def quicksort(arr,l,h):
    if l<h:
        head=iterate(arr,l)
        tail=iterate(arr,h)
        print('call')
        mid=partition(l,h,head,tail)
        print(mid,'mid')
        quicksort(arr,mid+1,h)
        quicksort(arr,l,mid-1)
        return arr
def partition(l,h,head,tail):
    pivot=head
    print('in')

    display(head)
    while l<h:
        while l<h and head.data<=pivot.data:
            l+=1  
            head=head.next
        while h>=l and  tail.data>pivot.data:
            h-=1
            tail=tail.prev
        if l<h:
            print('in')
            temp=tail.data
            tail.data=head.data
            head.data=temp            
            head,tail=tail,head
    print(tail.data,pivot.data)
    print('out')
    temp=tail.data
    tail.data=pivot.data
    pivot.data=temp
    print(tail.data,pivot.data)
    return h

l=Linkedlist()
x=[2,1,4,3,6,5,0]
for i in x:
    l.insert(i)
l.display()
quicksort(l.head,0,l.length()-1)
l.display()