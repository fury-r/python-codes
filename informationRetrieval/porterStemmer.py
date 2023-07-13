
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

def posting_lists(files,docs,path,name,flag):
    vocab=sorted([i  for i in set(word_tokenize(" ".join(docs).lower())) if i not in string.punctuation ])

    matrix={}
    
    for i in vocab:
        value=i
        if flag:
            value=PorterStemmer(i)
            print(i,value)
        matrix[value]=[]
        for j in  range(len(files)):
                
                with open(path+"/"+files[j],'r') as f:
                    x=word_tokenize(f.read().lower())
                    if i in x:
                        matrix[value].append(j+1)
    json_object=json.dumps(matrix)
    with open(name+".json",'w') as f:
        f.write(json_object)


    return matrix 
def PorterStemmer(d):
    rules={
        'ational':'ate',
        'tional':'tion',
        'ement':1,

        'sses':'ss',
        'ies':'i',
    }
    for k,v in rules.items():
        
        word=d[len(d)-len(k):len(d)]
        if word==k :
            if v==1:
                if len(d[:len(d)-len(k)])==1:
                    return d
                else:
                    return d[:len(d)-len(k)]
                    
            return d[:len(d)-len(k)]+v

    return d
def perform_query(query):
    matrix={}
    with open('index2.json','r') as f:
        matrix=json.load(f)
    p=set()
    for i in word_tokenize(query):
        for j in matrix[PorterStemmer(i)]:
            p.add(j)
    print(p)
           
path='exp'
docs,files=get_files(path)
vocab=create_vocab(docs)

posting_lists(files,docs,path,'index1',False)
posting_lists(files,docs,path,'index2',True)

perform_query(input('Query '))