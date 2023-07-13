def fib_iterative(n):
    a,b=0,1
    for i in range(0,n+1):
        print(a)

        a=b+a
        a,b=b,a
    return a
def fib_recursive(n):
    if n<=1: return n
    return fib_recursive(n-1)+fib_recursive(n-2)
a=int(input('Number '))

print(fib_recursive(a))
fib_iterative(a)