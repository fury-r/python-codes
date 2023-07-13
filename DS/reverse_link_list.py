class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.l = 0

    def insert(self, data):
        n = Node(data)
        h = self.head
        if(self.head == None):
            self.head = n
            self.tail = n
        else:
            while h.next != None:
                h = h.next
            h.next = n
            self.tail = n
        self.l += 1

    def display(self):
        tmp = self.head
        while tmp.next != None:
            print(tmp.data)
            tmp = tmp.next
        print(tmp.data)

    def remove(self, p):
        tmp = tmp1 = self.head
        if(p >= 0 and p <= self.l):
            for i in range(p):
                tmp1 = tmp
                tmp = tmp.next
            tmp1.next = tmp.next
            self.l -= 1

    def reverse_linklist2(self):
        prev = self.head
        current = self.head.next
        front = current.next
        while front != None:
            current.next = prev
            prev = current
            current = front
            prev = front.next
            print("i")
        current.next = prev
        self.head.next = None
        self.head = current

    def reverse_linklist(self):
        while self.head.next != None:
            tmp1 = tmp2 = tmp3 = self.head
            while tmp2.next != None:
                tmp1 = tmp2
                tmp2 = tmp2.next
            tmp2.next = tmp1
            tmp1.next = None
        self.head = self.tail
        self.tail = tmp3

    def get_length(self):
        i = 0
        head = self.head
        while head.next != None:
            head = head.next
            i += 1
        
        return i+1

    def get_middle(self):
        slow = fast = self.head
        while True:
            if fast.next==None or fast.next.next==None:break
            slow = slow.next
            fast = fast.next.next
        print(slow.data,'mid')

    def reverse_k_nodes(self, k):
        a = self.get_length()
        start = tmp = temp = self.head
        tail = self.head
        m = 0
 
        p=0
        while k<=a:
            tmp1=tmp2=self.head
            start=tmp=tail
            for i in range(1,k):
                temp=tmp
                tmp=tmp.next
            tail=tmp.next
            prev_point=temp.next
            while start.next!=tail:
                tmp1=tmp2=start
                while tmp2.next!=tail:
                    tmp1=tmp2
                    tmp2=tmp2.next
                tmp2.next=tmp1
                tmp1.next=tail
            a-=k     
            if(m==0):
                self.head=tmp
                m+=1
            else:
                m=+1
                prev.next=prev_point
            prev=tmp1
       
            


                

l=linklist()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)
l.insert(7)
l.insert(8)
l.display()
print(" ")

l.get_middle()
l.get_length()
# l.reverse_linklist()
l.reverse_k_nodes(2)
print("reversed ")
l.display()
