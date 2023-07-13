import os
from nltk.tokenize import word_tokenize

path = "exp1/"
files = os.listdir(path)

docs,file,documents = [],"",[]

for i in files:
    if(i.endswith(".txt")):
        file = file + " " + open(path+i,"r").read()
        docs.append(word_tokenize(open(path+i).read().lower()))
        documents.append(i)

val = sorted(set(word_tokenize(file)))+['apple','ape','chapel','applet','frappe','pea']
print(val)
print(end="\n")

newVal = []
for i in val:
    i = ''.join(("$",i,"$"))
    newVal.append(i)

word = input("Enter a mis-spelled word : ")
n = int(input("Enter the n value to generate n gram : "))
n_grams, word_n_grams = [],[]

# making n - gram of the unique words in the doc file
for i in newVal:
    for j in range(len(i)-1):
        s = ''
        if(j+n < len(i)):
            for k in range(j,j+n):
                s += i[k]
        n_grams.append(s)

# making n - grams of the input word 
for i in range(len(word)-1):
    s = ''
    if(i+n < len(word)+1):
        for k in range(i,i+n):
            s += word[k]
    word_n_grams.append(s)

n_gram_matrix = {
    key: []
    for key in n_grams
}

word_gram_matrix = {
    key : []
    for key in word_n_grams
}

# making the posting list for the new n - gram dictionary
for key, value in n_gram_matrix.items():
   for i in newVal:
    if(key in i):
        n_gram_matrix[key].append(i)

print(end="\n")   
print("The n - gram of our entire lexicon is : ") 
print(n_gram_matrix)
print(end="\n")

# checking if the broken word is present in our global dictionary
for key, value in word_gram_matrix.items():
    if(key in n_gram_matrix):
        for i in range(len(n_gram_matrix[key])):
            value.append(n_gram_matrix[key][i])

print("Mis-spelled query term posting list : ")
print(word_gram_matrix)
print(end="\n")

words = []
total_words = 0
for key, value in word_gram_matrix.items():
    for i in range(len(value)):
        if(value[i] not in words):
            total_words += 1
            words.append(value[i])

words_matrix = {
    key : []
    for key in words
}

for key, value in words_matrix.items():
    for k, v in word_gram_matrix.items():
        if key in v:
            value.append(1) # this append is like adding to a counter i.e counter += 1

max_jaquard_cofficient  = 0
jaquard_cofficient_word = ""
for key, value in words_matrix.items():
    temp = len(value)/total_words
    print("JC for : ", key, " is : ", temp)
    if(temp > max_jaquard_cofficient):
        max_jaquard_cofficient = temp
        jaquard_cofficient_word = key

print("Did you mean : ", jaquard_cofficient_word.replace("$",""))