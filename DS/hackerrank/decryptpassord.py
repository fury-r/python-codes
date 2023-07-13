
def decryptpassword(s):
    n='123456789'
    c=''
    for i in s:
        if i in n:
            c+=i
    p=''
    for i in s:
        if i not  in c:
            p+=i
    s=p
    c=c[::-1]
    for i in c:
        s=s.replace('0',i,1)
        print(i)
    while True:
        if '*' in s:
            print(s)
            index=s.index('*',1)
            
            p=s[:index]
            p=p[-2:]
            s=s.replace(p[-2:],p[::-1])
            print(s)
            s=s.replace('*','',1)
        else:
            break
    print(s)
decryptpassword('51Pa*0Lp*0e')