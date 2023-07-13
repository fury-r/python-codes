def generate(num):
    for i in range(num):
        yield i
g=generate(100)
next(g)
next(g)
print(next(g))
print(next(g))