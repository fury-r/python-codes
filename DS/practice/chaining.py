class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def Chaining(arr,size):
    result=[None]*size
    table={}
    for i in arr:
        index=(2*i+3)%size
        if result[index]==None:
            n=Node(i)
            result[index]=n
        else:
            p=result[index]
            while p.next!=None:p=p.next
            p.next=Node(i)
        table[i]=index
    print(result,table)
    
Chaining([3,2,9,6,11,13,7,12],10)