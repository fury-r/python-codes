def rabinkarp(t,p,q):
    sort=sorted(list(set(t)))
    table_value={sort[i]:str(i+1) for i in range(len(sort))}
    hash=int("".join([table_value[i] for i in p]))%q
    s=len(t)-len(p)
    for i in range(s+1):
        text=t[i:i+len(p)]
        value=int("".join([table_value[i] for i in text]))%q
        if value==hash:
            if text==p:
                print("Valid hit at ",i)
            else:
                print("Spurious hit at ",i)
t='AABAACAADAABAABA'
p='AABA'
q=int(input("Enter the prime number to be used: "))
rabinkarp(t,p,q)

