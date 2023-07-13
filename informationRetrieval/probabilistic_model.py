
import json
import string

from nltk.tokenize import word_tokenize

import os

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
def create_vocab(files):
    vocab=list(set([ i for i in word_tokenize(" ".join(files)) if i not in string.punctuation] ))
    return vocab

def create_term_freq(doc,filename):
    print(filename)
    vocab=create_vocab(filename)

    term_matrix={}
    for i in vocab:
        s=[]
        for j in range(len(doc)):
            s.append(doc[j].count(i))
        term_matrix[i]=s

    return term_matrix
def judge_rule(n,query,docs,filename):
    relevance={
        query:{}
    }
    print(docs)
    for k,v in docs.items():
        relevance[query][k]=[]
        for i in range(n):
            relevance[query][k].append(input())
    display(relevance,"judge rule")
    with open(filename+'.json','w') as f:
        f.write(json.dumps(relevance))
def get_relevant_docs(query,filename):
    relevance={}
    ranked=[]
    with open(filename+'.json','r') as f:
        relevance=json.load(f)

    for k,v in relevance[query].items():
        temp=[k]
        temp.append(v.count('0')/len(v))
        temp.append(v.count('1')/len(v))
        ranked.append(temp)
    print(ranked,"ranked")
    return sorted(ranked,key=lambda item:item[2],reverse=True)
def get_document(query,path,files):
    docs={

    }
    for i in files:
        with open(path+"/"+i ,'r') as f:
            x=f.read().lower()
            for j in word_tokenize(query):
                if j in x:
                    docs[i]=x
    return docs
def display(matrix,name):
    print("--------------------------------"+name+"------------------")
    for k,v in matrix.items():
        print(f'{k} {v}')
path='exp2'
docs,files=get_files(path)
vocab=create_vocab(docs)
x='relevance'
query=input("query ")
retrieved=get_document(query,path,files)
print(retrieved)
#n=input("judges ")
n=2
judge_rule(n,query,retrieved,x)
print(get_relevant_docs(query,x)[0][0])
#matrix=posting_lists(_,docs,path,name,True)
