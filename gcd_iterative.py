def gcd(a,b):
    q,r=0,0
    while b>0:
        q=b
        r=a%b
        a=q
        b=r
    return a
print (gcd(10,15))