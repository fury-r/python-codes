import math
def encryption(s):
    root=math.sqrt(len(s))
    ciel=math.ceil(root)
    floor=math.floor(root)

    if ciel<3:
        ciel=3
    if floor<3:
        floor=3
    c=0
    a=[]
    b={i:'' for i in range(ciel)}
    x=[]
    print(floor,ciel)
    for i in range(floor):
        a=[]
        v=0
        while v<ciel and c<len(s):
            b[v]+=s[c]
            a.append(s[c])

            v+=1
            c+=1
        x.append(a)
    for i in x:
        print(i)
    return " ".join(b.values())   
encryption('roqfqeylxuyxjfyqterizzkhgvngapvudnztsxeprfp')
#rlyzat oxqkps quthvx fyegue qxrvdp ejinnr yfzgzf

#rlyzatp oxqkps quthvx fyegue qxrvdp ejinnr yfzgzf