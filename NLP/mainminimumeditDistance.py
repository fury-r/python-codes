from nltk.corpus import words
# import nlkt
# nlkt.download('words')
def minimumEditDistance(string1):
    main=words.words()
    #main=['execution','maintain','tension','intentionally']
    string1='#'+string1
    final={}
    #main=main[:10000]
    x=1
    for string2 in main:
        string2='#'+string2
        if len(string2)>=len(string1):
            l=[[i] for i in  range(len(string1))]
            for i in range(1,len(string2)):
                l[0].append(i)
            if x:
                print(l)
                x=0
            for i in range(1,len(string1)):
                for j in range(1,len(string2)):
                    if string1[i]==string2[j]:
                        l[i].append(l[i-1][j-1])
                    else:
                        minimum=[l[i-1][j]+1,l[i][j-1]+1,l[i-1][j-1]+2]
                        minimum=sorted(minimum)
                        l[i].append(minimum[0])
            final[string2]=l[-1][-1]
            #final={k:v for k,v in sorted(final,reverse=True)}
    final = [[k,v] for k,v in  sorted(final.items(), key=lambda x: x[1])  ] 
    print(f"Processed words:{len(final)}\nMinimum:{final[0]}\n{final[0][0][1:]}")
minimumEditDistance(input('String 1: '))
#minimumEditDistance('intention','execution')