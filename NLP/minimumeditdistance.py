from nltk.corpus import words

def minimumEditDistance(string1):
    main=words.words()
    #main=['execution','maintain','tension','intentionally']
    string1='#'+string1
    final={}
    for string2 in main:

        string2='#'+string2
      # print(len(string2),len(string1),string1,string2)

        if len(string2)>=len(string1):
            l=[[i] for i in  range(len(string1))]
            for i in range(1,len(string2)):
                l[0].append(i)
            for i in range(1,len(string1)):
                for j in range(1,len(string2)):

                    if string1[i]==string2[j]:
                        l[i].append(l[i-1][j-1])
                    else:
                        minimum=[l[i-1][j]+1,l[i][j-1]+1,l[i-1][j-1]+2]
                        minimum=sorted(minimum)
                        l[i].append(minimum[0])
            k=reversed(l)


            # for i in k:
            #     p=''
            #     for j in i:
            #         p+=str(j)+' | '
            #     print('-'*len(p))
            #     print(p)
            #     p=''
            p=l[len(string1)-1][len(string2)-1]
            m=len(string1)-1
            n=len(string2)-1
            result=[]
            c=m+1 if m<n else n+1
            while m>0 and n>0:
                if string1[m]==string2[n]:
                    result.append(l[m-1][n-1])
                    m=m-1
                    n=n-1
                else:
                    minimum=[[l[m][n-1],m,n-1],[l[m-1][n],m-1,n],[l[m-1][n-1],m-1,n-1]]
                    minimum=sorted(minimum)
                    result.append(minimum[0][0])
                    n=minimum[0][2]
                    m=minimum[0][1]
            maxvalue=sorted(result)

            final[string2]=maxvalue[-1]
            #final={k:v for k,v in sorted(final,reverse=True)}
        final ={ k:v for k,v in  sorted(final.items(), key=lambda x: x[1])  }  
    print(final)
minimumEditDistance(input('String 1: '))
#minimumEditDistance('intention','execution')