from operator import rshift
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
def bagofword(arr):
    stop=stopwords.words('english')
    result=[]
    regex = re.compile('[@_!#$%^&,*()<>?/\|}{~:]')
    for i in arr:
        token=word_tokenize(i)
        result.append(' '.join([j.lower() for j in token if j.lower()  not  in  stop and  regex.search(j)==None ]) )
    final={i:{}  for i in range(0,len(arr)) }
    main1=' '.join(result).split(' ')
    main=[]
    for i in main1:
        if i not in main:
            main.append(i)
    print(f'Vocabulary {main}')
    print(result)
    for i in range(0,len(result)):
        for j in main:
            final[i][j]=result[i].count(j)
    for k,v in final.items():
        print('\nSentence no',k+1,'\n')
        for i,j in v.items():
            print(f'{i} - {j}')
bagofword(['Welcome to Great Learning,Now start learning','Learning is a good practice'])