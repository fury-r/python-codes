def matchingStrings(strings,queries):
    l=[]
    for i in queries:
        c=0
        for j in strings:
            if(j == i ):
                c+=1
        l.append(c)
    return l       
print(matchingStrings(['ab','ab','abc'],['ab','abc','bc']))