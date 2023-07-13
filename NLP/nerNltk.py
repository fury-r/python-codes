import nltk
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')

nltk.download("state_union")

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
sent='a.txt'
train_text=state_union.raw()
sample_text=state_union.raw('2006-GWBush.txt')


custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
tokenized=custom_sent_tokenizer.tokenize(sample_text)

try:
    for i in tokenized:
        words=nltk.word_tokenize(i)
        tagged=nltk.pos_tag(words)
        namedEnt=nltk.ne_chunk(tagged,binary=False)
        namedEnt.draw()
except:
    pass