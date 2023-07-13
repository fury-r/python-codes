


def boyermore(text,pattern):
    table_value={i:max(1,len(text)-text.rfind(i)-1) for i in text}
    c=0
    check=text[c:len(pattern)]
    print(len(pattern),len(check))
    while len(check)==len(pattern):
        flag=1
        if check==pattern:
            return "Match found",check,pattern
        for i in reversed(range(len(pattern))):
            if check[i]!=pattern[i]:
                c+=table_value[check[i]]
                flag=0
                break
        if flag:
            c+=table_value['*']
        check=text[c:c+len(pattern)]
    return 'Not found'
    
    
print(boyermore('This is a test','test'))

