def naive(t,p):
    s=len(t)-len(p)
    for i in range(0,s+2):
        if p==t[i:i+4]:
            print(f"pattern matches at {i}")

t='000010001010001'
p='0001'
naive(t,p)