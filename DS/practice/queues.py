class Queue:
    def __init__(self,main,wait):
        self.main=[]
        self.waiting=[]
        self.main_size=main
        self.wait_size=wait
    def insert(self,data):
        if len(self.main)<self.main_size:
            self.main.append(data)
        elif len(self.waiting)<self.wait_size:
            print('In waiting')
            self.waiting.append(data)
    def dequeue(self):
        if len(self.main)>0:
            self.main.pop(0)
            if len(self.waiting)>0:
                wait=self.waiting.pop(0)
                print('From waiting to main')
                self.main.append(wait)
    def display(self):
        print(f'main:{self.main}\nwaiting:{self.waiting}')


queue=Queue(3,2)
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.insert(5)
queue.display()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
