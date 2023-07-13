def jobs(j,d,p,n):
    m=[[p[i],j[i],d[i]] for i in range(0,5)]
    m.sort(reverse=True)
    print(m)
    d=n
    c=[]
    for i in range(0,n):
        if(d-m[i][2]>=0):
            d=d-m[i][2]
            c.append(m[i][1])
    return f"{c}"
jobld=['A','B','C','D','E']
deadline=[2,1,2,1,3]
profit=[100,19,27,25,15]
n=5
print(jobs(jobld,deadline,profit,n)) 