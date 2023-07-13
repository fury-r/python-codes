
#need improvement
def revString(a):
    result=''
    vowels='aieou'
    p=[a[i] for i in range(len(a)) if a[i] not in vowels]
    x=[i for i in range(len(a)) if a[i] not in vowels][::-1]
    p=[[p[i],x[i]] for i in range(len(p))][::-1]
    for i in range(len(p)):
        id1=p[i][1]
        if i ==len(p)-1:
            result+=p[i][0]+a[id2+1:]
        else:
            id2=p[i+1][1]
            result+=p[i][0]+a[id1+1:id2]
            print(result,a[id1+1:id2-1])
            

    return result

#optimal way
def revStringOpt(a):
    h,t=0,len(a)-1
    a=list(a)
    vowel='aieou'
    while h<t:
        if a[h] not  in vowel and a[t] not in vowel:
            a[h],a[t]=a[t],a[h]
            h+=1
            t-=1
        else:
            if a[h] in vowel:
                h+=1
            if a[t] in vowel:
                t-=1
    return "".join(a)
print(revString('rajeev'))
print(revStringOpt('rajeev'))