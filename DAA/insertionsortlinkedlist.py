

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return 1
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = new

        return 1

    def display(self):
        temp, l = self.head, []
        while temp:
            l.append(temp.data)
            temp = temp.next
        print(l)

    def length(self):
        i = 0
        temp = self.head
        while temp:
            temp = temp.next
            i += 1
        return i


def insertionSort(head):

    sorted = None

    current = head
    while (current != None):

        next = current.next

        sorted = sortedInsert(sorted, current)

        current = next

    head = sorted
    return head


def sortedInsert(head, node):

    current = None

    if (head == None or head.data >= node.data):

        node.next = head
        head = node

    else:

        current = head
        while (current.next != None and
               current.next.data < node.data):

            current = current.next

        node.next = current.next
        current.next = node

    return head


def iterate(arr, n):
    temp = arr
    while n > 0 and temp.next:
        temp = temp.next
        n -= 1

    return temp


def binarySearch(arr, f, l, h):

    if l<=h:
        mid = l+(h-l)//2
        x = iterate(arr, mid)
        if x.data == f:
            return 'Found'
        if f > x.data:
            return binarySearch(arr,f, mid+1, h)

        else:
            return binarySearch(arr,f, l, mid-1, )
    else:
        return 'Not There'

x = [64, 34, 25, 12, 22, 11, 90]


l = Linkedlist()
for i in x:
    l.insert(i)
p = insertionSort(l.head,)
l.head = p
l.display()
print(binarySearch(p,int(input('Search Element: ')), 0, l.length()-1))
