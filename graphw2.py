def adj(l):
    s,temp=len(l),[]
    for i in range  (0,s):
        m,q=0,[]
        a=l[i][0]
        if a not in temp:
            temp.append(a)
            for j in range (0,s):
                if(a==l[j][0]):
                    m+=l[j][2]
                    q.append(l[j][1])
            print(f"{l[i][0]}  has {m} length  and {q} vertices")
l=[[0,1,2],[0,4,5],[1,2,9],[1,3,8],[1, 4,4],[2, 3,2]]
adj(l)
