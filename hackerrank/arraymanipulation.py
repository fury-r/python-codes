def manipulate(p,queries,x,n):
    if x<len(queries):
        i=queries[x]
        p[i[0]-1:i[1]]=list(map(lambda item: item+i[2],p[i[0]-1:i[1]]))
        return manipulate(p,queries,x+1,n)
    else:
        return max(p)

def arrayManipulation(n,queries):
    p=[0]*n
    return manipulate(p,queries,0,n)
def arrayManipulationIterative(n, queries):
    p=[0 for i in range(n)]

    for i in queries:
        #if i[0]<i[1] and len(i)==3 and i[1]<n:
        p[i[0]-1:i[1]]=list(map(lambda item: item+i[2],p[i[0]-1:i[1]]))
    #print(p)
    return max(p)

f=open("./testcase/array.txt",'r')
p=f.read()
p=p.splitlines()
result=[[int(j) for j in i.split(" ")] for i in p]
print(arrayManipulation(10000000,result))