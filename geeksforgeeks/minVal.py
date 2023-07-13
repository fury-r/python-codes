def minValue(self, a, b, n):
    a=sorted(a)
    b=sorted(b,reverse=True)
    s=0
    for i in range(n):
        s+=a[i]*b[i]
    return s