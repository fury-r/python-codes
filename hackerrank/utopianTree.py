def utopianTree(n):
    h=1
    for i in n:
        for j in range(i):
            h+=1
    return h