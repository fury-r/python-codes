import json
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def get_files(path):
    return os.listdir(path)


def get_content(path,files):
    content=[]

    for i in files:
        with open(path+"/"+i,'r') as f:content.append(f.read())

    return content

def get_vocab(files_text):
    vocab=[]
    for i in files_text:
        vocab.extend([j for j in word_tokenize(i)])
    return set(vocab)

def incidence_matrix(file_content,vocab,filename):
    matrix={}
    for i in vocab:
        matrix[i]=[]
        for j in file_content:
            if i in j:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    json_file=json.dumps(matrix)
    with open(filename+".json",'w') as f:
        f.write(json_file)


def and_operation(x,y):
    return x and y

def or_operation(x,y):
    return [ 1 if(x[i]==1 or y[i]==1) else 0 for i in range(len(x))]


def not_operation(x):
    return [0 if i==1 else 1 for i in x]


def perform_query(query,filename):
    matrix={}
    operations={
        'and':and_operation,
        'or':or_operation
    }
    with open(filename+".json",'r') as f:
        matrix=json.load(f)

    query=query.split(" ")

    i=0
    x,y='',''
    if query[i]=='not':
        x=not_operation(matrix[query[i+1]])
    else:
        x=matrix[query[i]]
    i+=1
    operation=None
    while i<len(query):
        if query[i] in ['and','or']:
            operation=operations[query[i]]
            i+=1
        if query[i]=='not':
            x=not_operation(x)
            i+=1
        elif query[i] not in ['and','or']:
            y=matrix[query[i]]
            i+=1
        if operation:
            x=operation(x,y)
        i+=1

    return x

path='../exp'

list_files=get_files(path)

text=get_content(path,list_files)

vocab=get_vocab(text)
filename='incidence'
incidence_matrix(text,vocab,filename)

query=input()
print(perform_query(query,filename))