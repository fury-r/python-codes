def isBalance(data):
    pairs='(){}[]'
    d={
        '[':0,
        '(':0,
        '{':0
    }
    while True:
        if data:
            a=data.pop(-1)
            if a=='(' or a=='{' or a=='[':
                d[a]+=1
            elif a=='}' or a==')' or a==']':
                d[pairs[pairs.index(a)-1]]-=1
        else:
            break
    for k,v in d.items():
        if v>0 or  v<0: 
            print('Problem with',k)
            print('not balance',d)
            return 0
    print('balanced')
    return 0

a=input()
a=[i for i in a]
isBalance(a)