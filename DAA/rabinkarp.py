def rabinkarp(t,p,prime):
    val=sorted(set(t))
    number={ val[i]:str(i+1) for i in range(len(val)) }
    s=len(t)-len(p)
    hash=int("".join([number[j] for j in p]))%prime
    for i in range(0,s+1):
        l=t[i:i+len(p)]
        x=int("".join([number[j] for j in l]))
        if x%prime==hash:
            if l==p:
                print("Valid hit at ",i)
            elif l!=p:
                print("Spurious hit at ",i)

t='AABAACAADAABAABA'
p='AABA'
prime=int(input("Enter the prime number to be used: "))
rabinkarp(t,p,prime)