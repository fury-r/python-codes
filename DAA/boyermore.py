def boyermore(t,p):
    table={k:max(1,len(p)-(p.rfind(k))-1)  for k in p}
    table['*']=len(p)
    c=0
    check=t[c:len(p)]
    print(table)
    while len(check)==len(p): 
        if check==p:
            return 'Match',check,p
        for i in reversed(range(len(check))):
            flag=1
            if check[i]!=p[i] and check[i] in table.keys(): 
                c+=table[check[i]]
                flag=0
                break
            elif check[i]!=p[i] :
                break
        if flag:
            c+=table['*']
        check=t[c:c+len(p)]

    return 'No Match'
            
            

            
#print(boyermore('This is a test','test'))
print(boyermore('This is a txcvest','test'))
