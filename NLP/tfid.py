from nltk.corpus import stopwords
import re
import math
def tfid(arr):
    stopword=stopwords.words('english')
    pattern=r'[@_!#$%^&*()<>.?/\|}{~:]'
    words=[]
    vocab=[]

    for i in arr:
        l=re.sub(pattern,' ',i).lower().split(" ")
        c="" 
        for j in l:
            if j not in stopword:
                c+=j+" "
        c=c[:len(c)-1]
        if c not in vocab:vocab.append(j)
        words.append(c)
        print(words)
    tf=[[words[j].count(i)/len(words[j].split(" "))   for j in range(len(words))] for i in vocab]
    id=[math.log(len(words)/sum([ x.count(i) for x in words]))  for i in vocab]
    result=[[ j*id[i]  for j in tf[i]] for i in range(len(tf))]

    for i in range(len(vocab)):
        print(f"{vocab[i]}:{result[i]}")
tfid(['He is a good boy',"She is a good girl","Boy and girl are good"])