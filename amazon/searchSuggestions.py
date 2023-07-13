import re
def searchSuggestions(repository, customerQuery):
    l=[]
    repository.sort()
    for i in range(len(repository)):

        c=[]
        o=0
        for j in repository:
            if(customerQuery[:i] in j ):
                if(o<3):
                    c.append(j)
                    o+=1
                c.sort()
        l.append(c)
        for i in l:
            print(i)
    return l
print(searchSuggestions(['code','codePhone','coddle','coddles','codes'],'coddle'))