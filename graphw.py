def adj(l):
    s,temp=len(l),[]
    for i in range  (0,s):
        a,m=l[i][0],[]
        if a not in temp:
            temp.append(a)
            for j in range (0,s):
                if(a==l[j][0]):
                    m.append(l[j][1])
                elif(a==l[j][1]):
                    m.append(l[j][0])
            print(f"{l[i][0]}  has {m}  vertices")
    for i in range  (0,s):
        a,m=l[i][1],[]
        if a not in temp:
            temp.append(a)
            for j in range (0,s):
                if(a==l[j][1]):
                    m.append(l[j][0])
                elif(a==l[j][0]):
                    m.append(l[j][1])
            print(f"{a}  has {m}  vertices")
l=[[0,1],[0,4],[1, 2],[1,3],[1, 4],[2, 3],[3,4]]
adj(l)