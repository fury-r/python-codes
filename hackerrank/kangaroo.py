def kangaroo(x1,v1,x2,v2):
    a=x1*x2
    if(a<10):
        a=10
    for i in range(0,a):
        x1+=v1
        x2+=v2
        if(x1==x2): return 'YES'
    return 'NO'
print(kangaroo(14 ,4,98, 2))