
def calcMinimumSteps(a,b):
    p=[]
    for i in range(len(a)):
        x=a[i]-b[i]
        if x>0:
            p.append(x)
    print(p)
    return sum(p)
T=int(input())
for i in range(T):
    x=list(map(int,input().split(" ")))
    
    m,n,p=x[0],x[1],x[2]
    arr=[]
    
    for i in range(m):
        arr.append(list(map(int,input().split(" "))))
    print(arr)
    print(calcMinimumSteps(arr[0],arr[1]))
            


