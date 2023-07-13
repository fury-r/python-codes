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

def posting_lists(files,docs,path,name,flag):
    vocab=sorted([i  for i in set(word_tokenize(" ".join(docs).lower())) if i not in string.punctuation ])
    if flag:
        stop=stopwords.words('english')

        vocab=[ i for i in vocab if i not in stop]
    matrix={}
    
    for i in vocab:
        matrix[i]=[]
        for j in  range(len(files)):
                
                with open(path+"/"+files[j],'r') as f:
                    x=word_tokenize(f.read().lower())
                    if i in x:
                        matrix[i].append(j+1)
    json_object=json.dumps(matrix)
    with open(name+".json",'w') as f:
        f.write(json_object)


    return matrix