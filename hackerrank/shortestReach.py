def shortestReach(n,edges,s):
    q=0
    l=c=[]
    f=t=[]
    for i in range(0,len(edges)):
        c=l=list(edges[i])
        temp=list(edges)
        temp.pop(i)
        h=0
        print(c)
        for j in temp:
            if(j[2]<c[2] and c[1]==j[0]):
                q+=j[2]
                c=j
                print(q,c)

            if(j[1]==l[1] and q<l[2]and  l[0] not in t):
                f.append(q)
                print(q,'in')
                t.append(l[1])

                h=1
        if(not h):
            print(c)
            f.append(l[2])
    return f

print(shortestReach(4,[[1,2,24],[1,4,20],[3,1,3],[4,3,12]],1))