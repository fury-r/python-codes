def foo(codeList,shoppingCart):
    x,y=0,2
    a=shoppingCart[x]
    b=shoppingCart[y]
    while True:
        if(a==b):
            return 1
        elif(y==len(shoppingCart)):
            return 0 
print(foo([['a','a'],['b',1,'b']],['o','a','a','b','o','b']))