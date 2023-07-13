def naive(t,p):
    s=len(t)-len(p)
    for i in range(s+1):
        if t[i:i+len(p)]==p:
            print("Matches at ",i)


t='000010001010001'
p='0001'

naive(t,p)