def rodcut(l,p,le):
    m=[]
    for i in range(0,8):
        a=int(8/l[i])
        if 8%l[i]==0 :
            m.append(a*p[i])
        else:
            m.append(a*p[i]+p[a-1])
    return f"{l} \n{m} \n{max(m)}"
n=8
l=[num for num in range (1,n+1)]
p= [1, 5, 8, 9, 10, 17, 17, 20] 
print(rodcut(l,p,n))
  
