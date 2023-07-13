import heapq
def cookies(k, a):
    c=0
    heapq.heapify(a)
    while a[0]<k and len(a)>1:
        c+=1
        m1,m2,=heapq.heappop(a),heapq.heappop(a)
        heapq.heappush(a,m1+2*m2)
    p=[k<=i for i in a].count(True)
    return c if p==len(a) else -1 

print(cookies(10,[1,1,1]))