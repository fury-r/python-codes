import os
import string
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
def incidence_matrix(documents):
    vocab=set(word_tokenize(" ".join(documents)))
    vocab_cleaned=[i for i in vocab if i not in string.punctuation]
    vocab_cleaned=sorted(vocab_cleaned)
    imatrix={}
    for i in vocab_cleaned:
        imatrix[i]=[1 if i in j else  0 for j in documents]

    
    return imatrix

def get_boolean_a_and_b(x,y):

   return [ 1 if x[i]==1 and y[i]==1 else 0 for i in range(len(x))]


def get_boolean_a_or_b(x,y):


   return [ 1 if x[i]==1 or y[i]==1 else 0 for i in range(len(x))]



def perform_query(matrix,query):
    p={
        'and':get_boolean_a_and_b,
        'or':get_boolean_a_or_b,
    }

    query=query.split(" ")
    i=0
    x,y='',''
    if query[i]=='not':
        x=[ 1 if i==0 else 0 for i in matrix[query[i+1]]]

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
            y=[ 1 if i== 0 else 0 for i in matrix[query[i]]]
        elif query[i] not in ['and','or']:
            y=matrix[query[i]]
            i+=1
        if operation:
            x=p[operation](x,y)
            operation=None
        i+=1

    return x

    
def get_files(path):
    p=os.listdir(path)
    book=[]
    for i in p:
        if i.endswith('.txt'):
            with open(path+"/"+str(i),'r') as f:
                book.append(f.read().lower())
    return book,p

list_document,files=get_files('exp1')
documents={
    i:files[i] for i in range(len(files))
}

x=incidence_matrix(list_document)

#get_boolean_a_and_b('sales','home',list_document)
a='sales'
b='july'

p={
    'and':get_boolean_a_and_b,
    'or':get_boolean_a_or_b,
}
query=input('query ').lower()

x=perform_query(x,query)
print(x)
for i in range(len(x)):
    if x[i]==1:
        print(documents[i])