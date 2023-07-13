
def reverse_words_order_and_swap_cases(sentence):
    p=sentence.split(' ')
    l=[]
    
    for i in p:
        c=''
        for j in range(0,len(i)):
            if i[j].isupper():
                c+=i[j].lower()
            else:
                c+=i[j].upper()
        l.append(c)
        print(l)
    s=''
    l.reverse()
    for i in l:
        s+=i+' '
    s=s[:-1]
    print(s)
    return s
a=reverse_words_order_and_swap_cases('aWESOME is cODING')
print(a)