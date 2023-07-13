


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
def getstart(temp):
    while temp.prev!=None:
        temp=temp.prev
    return temp
def length(arr):
    c=0
    while arr:
        arr=arr.next
        c+=1
    return c
def bubblesort(l):
    temp=length(l)
    for  i in range(temp):
        temp1=getstart(l)
        temp2=temp1.next
        while temp2!=None:
            if temp1.data>temp2.data:
                """print(temp1.data,temp2.data)
                prev=[temp1.prev,temp2.prev]
                next=[temp1.next,temp2.next]
                temp1.prev,temp2.prev=prev[1],prev[0]
                temp1.next,temp2.next=next[1],next[0]
                if temp1.prev:
                    prev[1]=temp1 
                if temp2.prev:
                    prev[0]=temp2
                if temp1.next:
                    next[0]=temp2
                if temp2.next:
                    next[1]=temp1 
                temp1,temp2=temp2,temp1
                print(temp1.data,temp2.data) """
                temp1.data,temp2.data=temp2.data,temp1.data

            temp1=temp2
            temp2=temp2.next   
    return getstart(l)
p=[11,12,3,45,56,3,3,3,1,5]
l=LinkedList()
for i in p:
    l.insert(i,l.head)
l.display(l.head)
print('------------------------------------')
l.head=bubblesort(l.head)
l.display(l.head)