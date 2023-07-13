
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

class Linklist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if  not self.head:
            self.head=Node(data)
            return 1
        temp=self.head
        while temp.next!=None:temp=temp.next
        temp.next=Node(data)
        return 1
    def display(self):
        temp=self.head
        l=[]
        while temp!=None:
            l.append(temp.data)
            temp=temp.next
        print(l)

def getLinkedListLength(l):
    c=0
    while l!=None:
        c+=1
        l=l.next
    return c
def dividelist(head,n):
    temp=head
    temp3=head
    temp2=head
    for i in range(n):
        temp3=temp2
        temp2=temp2.next
    temp3.next=None
     
    return [temp,temp2]

def mergesort(left,right):
    l=Linklist()

    while left!=None and right!=None:
        if left.data<right.data:
            l.insert(left.data)
            left=left.next
        else:
            l.insert(right.data)
            right=right.next
    if  left:
        while left:
            l.insert(left.data)
            left=left.next
    if  right:
        while right:
            l.insert(right.data)
            right=right.next
    return l.head
def divide(arr):
    p=getLinkedListLength(arr)
    if p>1:
        mid=p//2
        partition=dividelist(arr,mid)
        left=divide(partition[0])
        right=divide(partition[1])
        return mergesort(left,right)
    else:
        return arr
x=[2,1,4,3,6,5,0]
l=Linklist()
for i in x:
    l.insert(i)
l.display()
x=divide(l.head)
l.head=x
print('Result')
l.display()