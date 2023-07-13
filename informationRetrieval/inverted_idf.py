import json
import os
import string
from nltk.tokenize import word_tokenize
import string

from nltk.corpus import stopwords

def posting_list(docs,flag,filename):
    vocab=sorted([i  for i in set(word_tokenize(" ".join(docs).lower())) if i not in string.punctuation ])
    if flag:
        stop=stopwords.words('english')

        vocab=[ i for i in vocab if i not in stop]
    matrix={}
    for i in vocab:
        matrix[i]=set()
        for j in  range(len(docs)):
            if i in word_tokenize(docs[j].lower()):
                matrix[i].add(j+1)
        matrix[i]=list(matrix[i])
    print(matrix)
    json_matrix=json.dumps(matrix)
    with open(filename+".json",'w') as f:
        f.write(json_matrix)

def get_boolean_a_and_b(x,y):

    return x & y


def get_boolean_a_or_b(x,y):

   return x^ y


def query_matrix(query,filename):
    matrix={}
    with open(filename+".json",'r') as f:
        matrix=json.load(f)
    p={
        'and':get_boolean_a_and_b,
        'or':get_boolean_a_or_b,
    }

    query=query.split(" ")
    i=0
    x,y='',''
    if query[i]=='not':
        i+=1
        x=[ 1 if i==0 else 0 for i in matrix[query[i]]]

    else:
        x=matrix[query[i]]
    i+=1
    operation=None
    while i<len(query):
        if query[i]  in ['and','or']:
            operation=query[i]
            i+=1
        if query[i]=='not':
            i+=1

            y=matrix[query[i]]
            i+=1
            x=get_boolean_a_or_b(set(x),set(y))

            operation='and'
        elif query[i] not in ['and','or']:
            y=matrix[query[i]]
            i+=1

        if operation:
            x=p[operation](set(x),set(y))
            operation=None
        i+=1

    return x
    
def get_files(path):
    p=os.listdir(path)
    book=[]
    print(f"{p}  list of files ")
    for i in p:
        if i.endswith('.txt'):
            with open(path+"/"+str(i),'r') as f:
                book.append(f.read().lower())

    return book,p


docs,files=get_files('exp1')

#with stopwords
x=posting_list(docs,False,'inverted_idf')
#without stopwords
y=posting_list(docs,True,'inverted_idf')

query=input("Query ")

files=query_matrix(query,'inverted_idf')
print(files)