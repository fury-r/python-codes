from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize

text='''There are many techniques available to generate extractive summarization to keep it simple,
I will be using an unsupervised learning approach to find the sentences similarity  and rank them.
Summarization can be defined as a task of producing a concise and fluent sumnmary while preserving key information and overall meaning.
One benefit of this will be,you don't need to train and build  a model  prior start using it your project.
It's good  to understand Cosine similarity to make the best use of code you are going to see.
Cosine Similarity is a measure of similarity between two non-zero  vectors of an inner product space that measures the cosine of the angle between them.
Its measures cosine angle between vectors.
The angle will be 0 if sentences are similar'''

stopword=stopwords.words("english")
word_tokens=word_tokenize(text)
sent_tokens=sent_tokenize(text)
freqTable={}
sentVal={}
for i in word_tokens:
    word=i.lower()
    if word not in stopword:
        if word in freqTable:
            freqTable[word]+=1
        else:
            freqTable[word]=1


for sent in sent_tokens:
    for word,freq in  freqTable.items():
         if word in sent.lower():       
            if sent in sentVal:
                
                sentVal[sent]+=freq
            else:
                sentVal[sent]=freq
avg=sum(sentVal.values())/len(sentVal)
summary=''
for sent in sent_tokens:
    if sent in sentVal and (sentVal[sent])>1.2*avg:
        summary+=" "+sent
print('\n',summary)
