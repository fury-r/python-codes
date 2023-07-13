from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import nltk 
nltk.download('stopwords')
#regex_shortfrom $ and -
#tokenization
#remove stopword 
#lematization

t="That’s why we build Firefox, and all our products, to give you greater control over the information you share online and the information you share with us. We strive to collect only what we need to improve Firefox for everyone.In this Privacy Notice, we explain what data Firefox shares and point you to settings to share even less. We also adhere to the practices outlined in the Mozilla privacy policy for how we receive, handle and share information we collect from Firefox"
#p=word_tokenize.tokenize(t)
stop=stopwords.words('english')
full_text=word_tokenize(t)
sent=sent_tokenize(t)
print(f'sentence {sent}')
print(f'original size: {len(full_text)}\n{full_text}')
final=[]


for i in full_text:
    if i not in stop:
        final.append(i)


print(f'final size: {len(final)}\n{final}')

