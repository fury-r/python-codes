import json
import string

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
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

def ngrams(vocab,ngrams=2):
    result=[]
    result={word:[ "".join(j) for j in zip(*[word[i:] for i in range(ngrams)]) ] for word in vocab}
    ngram={}
    for k,v in result.items():
        for i in v:
            if i not in ngram.keys():
                ngram[i]=[k]
            else:
                ngram[i].append(k)
    return ngram

def jaccard(query,matrix,ngrams):
    query_grams=["".join(i) for i in zip(*[query[i:] for i in range(ngrams)])]
    print(query_grams)
    combined=[]
    union_set=set()
    for gram in query_grams:
        if gram in matrix.keys():
            if len(union_set)==0:
                union_set=set(matrix[gram])
            else:
                union_set.union(set(matrix[gram]))
            for i in matrix[gram]:
                combined.append(i)


    
    high=[-1,-1]
    for k in union_set:
        
        x=[k,combined.count(k)/len(union_set)]
        if x[1]==high[1]:
            high=x+high
        elif x[1]>high[1]:high=x

    print(high)


ngram=2
path='exp'
docs,files=get_files(path)
vocab=create_vocab(docs)+['apple','ape','chapel','applet','frappe','pea']
matrix=ngrams(vocab,ngram)

query=input("Query ")

jaccard(query,matrix,ngram)