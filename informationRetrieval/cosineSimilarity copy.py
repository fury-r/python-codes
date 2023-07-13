from fileinput import filename
import json
import math
import string
import sys
from fileInfo import get_files
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

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
            s.append(doc[j].count(i))
        term_matrix[i]=s

    return term_matrix


def log_frequency_weighting(term_matrix):
    log_matrix={}
    for k,v in term_matrix.items():
        p=[]
        for i in v:
            p.append(math.log10(1+i))
        log_matrix[k]=p
    return log_matrix

    
def length_normalization(matrix,n):
    normalized_matrix={}
    normalized=[]
    for i in range(n):
        x=sum([v[i]**2 for k,v in matrix.items()])
        normalized.append(x)
    for k,v in matrix.items():

        normalized_matrix[k]=[v[i]/math.sqrt(normalized[i]) for i in range(len(v))]

    return normalized_matrix



def cosine_similarity(query,normalized_matrix,docs):
    ranked_docs={}
    q=0
    for j in word_tokenize(query):
        q+=sum([l**2 for l in normalized_matrix[j]])
    
    for i in range(len(docs)):
        ranked_docs[docs[i]]=0
        d=0
        dot=0
        
        for k,v in normalized_matrix.items():
            d+=v[i]**2
        for j in word_tokenize(query):
            #q+=normalized_matrix[j][i]**2
            dot+=normalized_matrix[j][i]**2
        ranked_docs[docs[i]]=math.degrees(dot/(math.sqrt(q)*math.sqrt(d)))
    print(ranked_docs)

    ranked_docs={k:v for k,v in sorted(ranked_docs.items() , key= lambda item:item[1], reverse=True)}
    print(ranked_docs)
              
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
def display(matrix,name):
    print("--------------------------------"+name+"------------------")
    for k,v in matrix.items():
        print(f'{k} {v}')


       
path='exp'
docs,_=get_files(path)
print(docs)
name='vectorSpace'

matrix=posting_lists(_,docs,path,name,True)
term_matrix=create_term_freq(docs,name)
display(term_matrix,'tf')


log_term_matrix=log_frequency_weighting(term_matrix)
display(log_term_matrix,'log_term_matrix')

normalized_matrix=length_normalization(term_matrix,len(_))
display(normalized_matrix,'normalized_matrix')

query=input('query ')

ranked_docs=cosine_similarity(query,normalized_matrix,_)