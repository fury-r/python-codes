from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk 
nltk.download('wordnet')


#p=word_tokenize.tokenize(t)
lem=WordNetLemmatizer()
print(f"better {lem.lemmatize('beter')}")

