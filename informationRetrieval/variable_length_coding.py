import json
import os
import string
from unittest import result
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
    json_matrix=json.dumps(matrix)
    with open(filename+".json",'w') as f:
        f.write(json_matrix)


    
def get_files(path):
    p=os.listdir(path)
    book=[]
    print(f"{p}  list of files ")
    for i in p:
        if i.endswith('.txt'):
            with open(path+"/"+str(i),'r') as f:
                book.append(f.read().lower())

    return book,p

def gaps(posting):

    gaps_posting={}
    for k,v in posting.items():
        gaps_posting[k]=[v[0]]+[v[i]+v[i-1] for i in range(1,len(v))]


    return gaps_posting
def get_zeros(s):
    return '0'*(7-len(s))

def vbcode(v):
    result=[]
    for i in v:
        rem=i%128
        quo=i//128
        ct=0
        x=[]

        while ct!=1:
            if rem<=127:
                x.append(rem)

            if quo<=127:
                if quo==0:
                    ct=1
                else:
                    x.append(quo)
                    ct=1
            rem=quo%128
            quo=quo//128
        code=''
        x.reverse()
        for i in range(len(x)):
            binary=bin(x[i]).replace("0b","")
            if(i==len(x)-1):
                code+="1"+get_zeros(binary)+binary
            else:
                code+="0"+get_zeros(binary)+binary
        result.append(code)
    return "".join(result)


def display(matrix,name):
    print("--------------------------------"+name+"------------------")
    for k,v in matrix.items():
        print(f'{k} {v}')

def gamma_code(posting):
    gamma_posting={}
    for k,v in posting.items():
        gamma_posting[k]=[]
        for i in v:
            value1=bin(i).replace("0b", "")
            if(len(value1)>1):
                value1=value1[1:]
                value2="".join(['1' for i in range(len(value1))])+"0"
                gamma_posting[k].append(value2+value1)
            else:
                value1=0
                gamma_posting[k].append(0)
    
                


    return gamma_posting
def variable_posting(matrix):
    v_matrix={}
    for k,v in matrix.items():
        v_matrix[k]=vbcode(v)
    return v_matrix


docs,files=get_files('exp')

filename='inverted_idf'
#without stopwords
y=posting_list(docs,True,filename)
posting={}
with open(filename+".json",'r') as f:
    posting=json.load(f)
gamma_without_gaps=gamma_code(posting)
gaps_posting=gaps(posting)
gamma_gaps=gamma_code(gaps_posting)

print(gaps_posting)
display(gamma_gaps,"gamma")
print(gamma_without_gaps)

v_matrix=variable_posting(gaps_posting)
display(v_matrix,"variable_posting")

vbcode([824,5,214577])
