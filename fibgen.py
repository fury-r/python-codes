def fib(int):
    a=0
    b=1
    for i in range(0,int+1): 
        yield a+b
        b=b+a
        a=b-a


a=fib(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))