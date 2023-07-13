import heapq
q=int(input())
heap=[]
s=set()
def insert(x):
    heapq.heappush(heap,x)
    s.add(x)
def pop_item(x):
    s.discard(x)
        
def min(x):
    while heap[0] not in s:
        heapq.heappop(heap)
    print(heap[0])
    return heap[0]
opt={
    1:insert,
    2:pop_item,
    3:min
}
for i in range(q):
    x=list(map(int,input().split(" ")))
    opt[x[0]](0 if len(x)<2 else x[1])

