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

def permutermMatrix(vocab):
    matrix={}
    for i in vocab:
        k=i+'$'
        flag=False
        while k[-1]!='$' or flag==False:
            matrix[k]=i

            k=k[1:]+k[0]
            flag=True
    print(matrix)


path='../exp'

list_files=get_files(path)

text=get_content(path,list_files)

vocab=get_vocab(text)
filename='incidence'
permutermMatrix(vocab,)

