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

def insertNodeAtHead(llist,data):
    d=Node(data)
    d.next=llist
    return d
def printLinkedList(head):
    tmp=head
    while tmp!=None:
        print(tmp.data)
        tmp=tmp.next
def insertNodeAtPosition(head,data,position):
    n=Node(data)
    if(position==0):
        n.next=head
        return n
    else:
        tmp=head
        for i in range(0,position-1):
            tmp=tmp.next
        n.next=tmp.next
        tmp.next=n
def deleteNode(llist,position):
    if(position==0):
        head=llist.next
        llist.next=None
        return head
    else:
        tmp=tmp1=llist
        for i in range(0,position):
            tmp1=tmp
            tmp=tmp.next
        tmp1.next=tmp.next
def reverse(llist):
    head=tail=llist
    while tail.next!=None:
        tail=tail.next
    while head.next!=None:
        tmp1=tmp2=llist
        while tmp2.next!=None:
            tmp1=tmp2
            tmp2=tmp2.next     

        tmp2.next=tmp1
        tmp1.next=None
    llist=tail
    
    head=llist
    while head!=None:
        print(head.data)
        head=head.next
def compare_lists(llist1,llist2):
    o=p=0
    tmp1=llist1
    tmp2=llist2
    while llist1!=None:
        llist1=llist1.next
        p+=1
    while llist2!=None:
        llist2=llist2.next      
        o+=1
    while tmp1!=None and tmp2!=None:
        if(tmp1.data!=tmp2.data):
            return 0
        tmp1=tmp1.next
        tmp2=tmp2.next
    if(o==p):return 1
    return 0
def mergeLists(h1,h2):
    if(h1==None or h1==None):
        if(h1==None):return h2
        return h1
    if(h1.data<h2.data):
        h1.next=mergeLists(h1.next,h2)
        return h1
    h2.next=mergeLists(h2.next,h1)
    return h2
def getNode(llist,p):
    tmp1=tmp2=llist
    for i in range(p):
        tmp2=tmp2.next
    while tmp2!=None and tmp2.next!=None:
        tmp1=tmp1.next
        tmp2=tmp2.next
    return tmp1.data
def removeDuplicates(llist):
    tmp1=llist
    tmp2=llist.next
    while tmp2!=None:
        i=0
        print(tmp1.data,tmp2.data)
        if(tmp1.data==tmp2.data ):
            tmp1.next=tmp2.next
            tmp2=tmp2.next
            i=1
        if(i==0):
            tmp1=tmp1.next
            tmp2=tmp2.next
def has_cycle(head):
    if(head.next==None or head==None):return 0
    i=set()
    tmp=head
    while tmp.next!=None:
        if  tmp in i:
            return 1
        i.add(tmp)
        tmp=tmp.next
    return 0
        
    # tmp1=head.next
    # tmp2=head.next.next
    # while tmp2!=None:
    #     if(tmp1==tmp2):
    #         return 1
    #     tmp1=tmp1.next
    #     tmp2=tmp2.next.next
    # return 0
def findMergeNode(head1, head2):
    tmp1,tmp2=head1,head2
    while True:
        if(tmp1.next==None):tmp1=head1
        else:tmp1=tmp1.next
        if(tmp2.next==None):tmp2=head2
        else:tmp2=tmp2.next
        if tmp1==tmp2:
            break
    return tmp1.data
def sortedInsert(llist, d):
    tmp1=tmp2=llist
    n=Node(d)
    while tmp2.next!=None:
        if tmp1.data>d  and tmp2.data<d:
            break
        tmp1=tmp2
        tmp2=tmp2.next
    if(tmp1==llist):
        n.next=tmp2
        tmp2.prev=n
        return n
    if(tmp2.next==None):
        tmp2.next=n
        n.prev=tmp2
        return llist
    tmp1.next=n
    n.prev=tmp1
    n.next=tmp2
    tmp2.prev=n
    return llist

llist=SinglyLinkedList()
llist1=SinglyLinkedList()

llist1.insert_node(1)
llist1.insert_node(3)
llist1.insert_node(4)
llist1.insert_node(10)
sortedInsert(llist1.head,5)
printLinkedList(llist1.head)
# print(getNode(llist1.head,3))
# removeDuplicates(llist1.head)

# llist.insert_node(1)
# llist.insert_node(2)

print(" ")
# mergeLists(llist1.head,llist.head)
# printLinkedList(llist1.head)

# printLinkedList(llist.head)
# print(" ")
# reverse(llist.head)
# print(" ")
