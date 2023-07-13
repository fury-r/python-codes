def iterative(n):
    c=1
    for i in range(1,n+1):
        c*=i
    return c
def recursive(n):
    if n==0:
        return 1
    return n*recursive(n-1)

a=int(input('Number '))
print(f'recursive {recursive(a)}')
print(f'iterative {iterative(a)}')