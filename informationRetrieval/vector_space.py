import string
from nltk.tokenize import word_tokenize
import string
import json

from nltk.corpus import stopwords
import math
import os
def get_files(path):
    p=os.listdir(path)
    book=[]
    print(f"{p}  list of file")
    for i in p:
        if i.endswith('.txt'):
            with open(path+"/"+str(i),'r') as f:
                book.append(f.read().lower())

    return book,p
def posting_list(docs,flag,filename):
    print(docs,flag)
    vocab=sorted([i  for i in set(word_tokenize(" ".join(docs).lower())) if i not in string.punctuation ])
    if flag:
        stop=stopwords.words('english')

        vocab=[ i for i in vocab if i not in stop]
    matrix={}
    for i in vocab:
        matrix[i]=[]
        for j in  range(len(docs)):
            if i in word_tokenize(docs[j]):
                matrix[i].append(j+1)
    json_object=json.dumps(matrix)
    with open(filename+".json",'w') as f:
        f.write(json_object)


    return matrix
def count_occurence(term,doc):
    return doc.count(term)

def create_vocab(filename):
    vocab=[]
    print(filename)
    with open(filename+".json",'r') as f:
        vocab=json.load(f).keys()
    return list(vocab)

def create_term_freq(doc,filename):
    print(filename)
    vocab=create_vocab(filename)

    term_matrix={}
    for i in vocab:
        s=[]
        for j in range(len(doc)):
            s.append([j+1,doc[j].count(i)])
        term_matrix[i]=s

    return term_matrix
def idf_matrix(matrix,docs):
    idf={}
    print(matrix)
    for k,v in matrix.items():
        idf[k]=math.log10(docs/len(v))
    return idf
    


    
    


def apply_tf_idf(termfValues,idfValues):
    tf_idf={}
    
    for k,v in termfValues.items():
        x=[]
        for i in v:
            x.append([math.log10(1+i[1])*idfValues[k],i[0]])
        tf_idf[k]=x

    return tf_idf


def display(matrix,name):
    print("--------------------------------"+name+"------------------")
    for k,v in matrix.items():
        print(f'{k} {v}')
def score(query,matrix,n):
    print(n)
    docs=[]
    words=word_tokenize(query)
    for i in range(n):
        value=[]
        for j in words:
            if j in matrix.keys():
                value.append(matrix[j][i][0])
        if len(value)==len(words):
            docs.append([i+1,sum(value)])
    print(sorted(docs,key=lambda item:item[1],reverse=True))


docs,_=get_files('exp')
name='vectorSpace'

matrix=posting_list(docs,True,name)
term_matrix=create_term_freq(docs,name)
display(term_matrix,'tf')
idf=idf_matrix(matrix,len(docs))
display(idf,'idf')

p=apply_tf_idf(term_matrix,idf)
display(p,'TFidf')

query=input("Query ")
score(query,p,len(_))

#print(sorted(p[query],key=lambda item:item[0],reverse=True)[0])  