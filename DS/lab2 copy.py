

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class linklist:
    def __init__(self, l):
        self.head = None
        self.tail = None
        self.i = 0
        self.l = l
        self.loop = self.head

    def insert(self, data):
        head = self.head
        n = Node(data)
        if(self.i < self.l):
            if(head == None):
                self.head = n
                self.tail = n
                self.i = self.i+1
            else:
                self.tail.next = n
                self.tail = n
                self.i = self.i+1
        else:
            print(f"linklist is full {self.i}")

    def display(self):
        start = self.head
        while start.next != None:
            print(start.data)
            start = start.next
        print(start.data)

    def remove(self, a):

        if(a < self.i and a == 1):
            self.head = self.head.next
        elif(a == self.i):
            head = self.head
            for i in range(1, a-1):
                head = head.next
            head.next = None
            self.tail = head
        elif(a < self.i):
            tmp2 = self.head
            tmp1 = None
            for i in range(1, a):
                tmp1 = tmp2
                tmp2 = tmp2.next
            tmp1 = tmp2.next
            tmp2.next = None

    def break_loop(self):
        if(self.loop != None):
            start = temp = self.head
            meet = self.loop
            while start.next != meet:
                temp = meet
                start = start.next
                meet = meet.next
            temp.next = None
            self.loop = None

    def loop_insert(self, data, n):
        node = Node(data)
        if(n < self.i):
            pos = self.head
            for i in range(0, n-1):
                pos = pos.next
            self.tail.next = node
            self.tail = node
            self.tail.next = pos

    def detect_loop(self):
        slow = fast = self.head
        while fast != None:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                self.loop = slow.next
                return 'Loop Detected'
        return 'Loop not Detected'

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

    def find_middle(self):
        slow = fast = self.head
        while True:
            if fast == None or fast.next == None:
                break
            fast = fast.next.next
            slow = slow.next
        return slow.data

op = 0
l = linklist(100)


while True:
    op = int(input("1.Add\n2.Display\n3.Loop Insert\n4.Detect loop\n5.Find Middle\n6.Reverse\n7.Breakloop\n8.Remove\n9.Exit\n"))
    if(op == 1):
        a = int(input("enter a number \n"))
        l.insert(a)
    elif(op == 2):
        l.display()
    elif(op == 3):
        a = int(input("enter a number \n"))
        b = int(input("enter a position \n"))
        l.loop_insert(a, b)
    elif(op == 4):
        print(l.detect_loop())
    elif(op == 5):
        print(l.find_middle())
    elif(op == 6):
        l.reverse_linklist()
    elif(op == 7):
        l.break_loop()
    elif(op == 8):
        b = int(input("enter a position \n"))
        l.remove(b)
    elif(op == 9):
        break


# l.insert(1)
# l.insert(2)
# l.insert(3)
# l.insert(4)
# l.insert(5)
# l.insert(6)
# l.loop_insert(7,3)
# print(l.detect_loop())
# l.break_loop()
# l.display()

# l.reverse_linklist()
# l.display()

# print(l.find_middle(),'mid')
