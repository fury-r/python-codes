from nltk.corpus import stopwords

def ngrams(arr,ngrams=1):
    stop=stopwords.words("english")
    pattern='[@_!#$%^&*()<>.?/\|}{~:]'
    words=[[j for j in arr if j not in stop and j not in pattern] for i in arr]
    ngram=[]
    for i in words:
        temp=zip(*[i[j:] for j in range(ngrams) ])
        ngram.append([" ".join(n) for n in temp])
    print(ngram)
ngrams(['This is a good job. I will not miss it for anything','This is not good at all'],ngrams=2)