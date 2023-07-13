def als(p,e):
    l=[[0  for j in range(len(p[0])+1)] for i in  range(2)]
    table=[[0  for j in range(len(p[0])+1)] for i in  range(2)]
    x=[e[0]+p[0][0],e[1]+p[3][0]]
    l[0][0],l[1][0]=1,2
    table[0][0]=x[0]
    table[1][0]=x[1]
    exit=0
    for i in range(1,len(p[0])+1):
        if i==len(p[0]):
            x=[p[1][i-1]+table[0][i-1],p[2][i-1]+table[1][i-1]]
            l[0][i],l[1][i]=x.index(min(x))+1,x.index(min(x))+1
            table[0][i]=min(x)
            table[1][i]= min(x)     
        else:
            f1=[table[0][i-1]+p[0][i],table[1][i-1]+p[2][i-1]+p[0][i]]
            f2=[table[0][i-1]+p[1][i-1]+p[3][i],table[1][i-1]+p[3][i]]
            l[0][i]=f1.index(min(f1))+1
            l[1][i]=f2.index(min(f2))+1
            table[0][i]=min(f1)
            table[1][i]=min(f2)   
            exit=f1.index(min(f1)) 
    x=[l[exit][-1],exit,len(l[exit])]
    for i in reversed(range(len(l[0]))):
        x=[l[x[0]-1][i],i]
        print(f"station {x[1]} line {x[0]} ")
    print("minimum time ",table[-1][-1])     
 
p=[
    [7,9,3,4,8,4],
    [2,3,1,3,4,3],
    [2,1,2,2,1,2],
    [8,5,6,4,5,7]
]
e=[2,4]
als(p,e)

