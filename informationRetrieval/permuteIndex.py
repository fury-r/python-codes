
import json

import os
import string
from nltk.tokenize import word_tokenize
import string
import json

from nltk.corpus import stopwords

def get_files(path):
    p=os.listdir(path)
    book=[]
    print(f"{p}  list of file")
    for i in p:
        if i.endswith('.txt'):
            with open(path+"/"+str(i),'r') as f:
                book.append(f.read().lower())

    return book,p

def posting_list(files,docs,flag):
    print(docs,flag)
    vocab=sorted([i  for i in set(word_tokenize(" ".join(docs).lower())) if i not in string.punctuation ])
    if flag:
        stop=stopwords.words('english')

        vocab=[ i for i in vocab if i not in stop]
    matrix={}
    result=""
    for i in vocab:
        matrix[i]=[]
        for j in  range(len(docs)):
            if i in word_tokenize(docs[j]):
                matrix[i].append(j+1)
        result+="key: "+i+' '+f" freq: {len(matrix[i])}  posting: "+" ".join([str(x) for x in matrix[i]])+" \n"
    json_object=json.dumps(matrix)
    with open('stopwords.json' if flag else "normal.json",'w') as f:
        f.write(json_object)


    return matrix
def permute_index(filename):
    permute_matrix={}
    matrix={}
    with open(filename,'r') as f:
        matrix=json.load(f)
    for k,v in matrix.items():
        x=k+'$'

    
        for j in range(len(k)+1):
            x=x[1:len(x)]+x[0] 
            permute_matrix[x]=k
    print(permute_matrix)
    json_object=json.dumps(permute_matrix)
    with open("permuteIndex.json",'w') as f:
        f.write(json_object)
    return permute_matrix
def perform_query(query):
    x_query=query
    permutes={}
    with open("permuteIndex.json",'r') as f:

        permutes=json.load(f)

    keys=[]
    y_query=x_query+'$'


    if x_query.count('*')==1:
        while y_query[-1]!='*':
            y_query=y_query[1:len(y_query)]+y_query[0]   
        y_query="".join([i for i in y_query if i not in "*"])

        for k,v in permutes.items():
            if y_query in  k  and v not in keys:

                keys.append(v)
    else:
        split_on_ast=x_query.split("*")
        print(split_on_ast)

        for k,v in permutes.items():
            x=k
            count=0
            for i in split_on_ast:
                if i in x:
                    x.replace(i,'')
                    count+=1
            if count==len(split_on_ast) and v not in keys and (x[-2:]==x_query[-1]+"$" or x_query[-1]=='*') :
                keys.append(v)    

    print(keys)
docs,files=get_files('exp')
matrix=posting_list(files,docs,True) 


permute_index('stopwords.json')

query=input("Query ")
perform_query(query)