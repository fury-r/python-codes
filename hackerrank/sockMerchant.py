def sockMerchant(n,ar):
    s=set(ar)
    l={i:ar.count(i) for i in s}
    c=0
    q=sum([int(i/2) if(i%2==0) else int((i-1)/2)  if(i%2!=0 and i>1)   else 0  for k,i in l.items() ])
    print(q)
    for k,i in l.items():
        if(i%2==0):
            c+=i/2
        elif(i%2!=0 and i>1):
            c+=(i-1)/2
    return c
print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))