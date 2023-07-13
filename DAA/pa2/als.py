from cmath import tan


def als(sub,e):
    tables=[[0 for i in range(len(sub[0])+1)] for i in range(2)]
    lines=[[0 for i in range(len(sub[0])+1)] for i in range(2)]
    x=[sub[0][0]+e[0],sub[1][0]+e[1]]
    tables[0][0]=x[0]
    tables[1][0]=x[1]
    lines[0][0]=1
    lines[1][0]=2
    for i in range(len(sub[0])+1):
        if i==len(sub[0]):
            x=[sub[1][i-1]+tables[0][i-1],tables[1][i-1]+sub[0][i-1]]
            tables[0][i]=tables[1][i]=min(x)
            lines[0][i]=tables[1][i]=min(x)+1
        else:
            f1=[tables[0][i-1]+sub[0][i],tables[1][i-1]+sub[0][i]+sub[2][i]]
            f2=[tables[1][i-1]+sub[3][i],tables[0][i-1]+sub[1][i]+sub[3][i]]
            tables[0][i]=min(f1)
            tables[1][i]=min(f2)
            lines[0][i]=f1.index(min(f1))+1
            lines[1][i]=f2.index(min(f2))+1
            if min(f1)>min(f2):exit=1
            else:
                exit=2
    x=[lines[exit-1][-1],exit]
    for i in reversed(range(len(lines[0]))):
        x=[lines[x[0]-1][i],i]
        print(x)
    print(tables[exit-1][-1])
p=[
    [7,9,3,4,8,4],
    [2,3,1,3,4,3],
    [2,1,2,2,1,2],
    [8,5,6,4,5,7]
]
e=[2,4]

als(p,e)