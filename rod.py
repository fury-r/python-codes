def rodcut(l,p,n):
    temp,c,q=[],[],[]
    e=n-1
    for i in range(0,n):
        m,n,q=0,e,[]
        m,n=m+p[i],n-i
        while n>=1:
            temp=[p[num] for num in range(0,n)]
            a=temp.index(max(temp))
            n=n-a-1
            if(n==1):
                n,m=n-1,m+max(temp)+temp[0]
                break
            m+=max(temp)
        q=[m,a+1,i+1]
        c.append(q)
    return f"{max(c)} max profit From \n {c}"
n=8
l=[num for num in range (1,n+1)]
p= [1,5,8,9,10,17,17,20] 
print(rodcut(l,p,n))
