from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import re

def ngrams(arr,ngrams=1):
    stopword=stopwords.words('english')
    pattern=r'[@_!#$%^&*()<>.?/\|}{~:]'
    words=[  [ j for j in re.sub(pattern,' ',i).split(" ") if j not in stopword ]  for i in arr]
    ngram=[]
    for i in words:
        temp=zip(*[i[j:] for j in range(ngrams)])
        ngram.append([" ".join(n) for n in temp])
    print(ngram)
ngrams(['This is a good job. I will not miss it for anything','This is not good at all'],ngrams=2)