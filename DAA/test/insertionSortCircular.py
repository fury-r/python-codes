from dataclasses import dataclass


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        if not self.head:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            new=Node(data)
            temp.next=new
        
def display(head):
    while head:
        print(head.data)
        head=head.next
def insertionSort(head):
    temp=head
    sorted=None
    while temp:
        next=temp.next
        sorted=sort(sorted,temp)
        temp=next
    head=sorted
    return head
def sort(head,node):
    if head==None or head.data>=node.data:
        node.next=head
        head=node
    else:
        cur=head
        while cur.next and cur.next.data<node.data:
            cur=cur.next
        node.next=cur.next
        cur.next=node
    return head
        

p=[100,1,1,2,3,4,45,6]
l=CircularLinkedList()
for i in p:
    l.add(i)
display(l.head)
l.head=insertionSort(l.head)
display(l.head)