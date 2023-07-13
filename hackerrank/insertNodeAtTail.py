class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_node(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n
    def display(self):
        tmp=self.head
        while tmp!=None:
            print(tmp.data)
            tmp=tmp.next
        print('w')
def insertNodeAtTail(head, data):
    n=Node(data)
    tmp=head
    print('w')
    print(head)
    if(head==None):
        return n
    while tmp.next!=None:
        tmp=tmp.next
    tmp.next=n
    return n

l=SinglyLinkedList()
head=l.head
a=insertNodeAtTail(head,141)
x=insertNodeAtTail(head,302)
insertNodeAtTail(head,164)