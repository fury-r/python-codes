import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
nltk.download('maxent_ne_chunker')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
nltk.download('treebank')
nltk.download('maxent_treebank_pos_tagger')
sentence='We saw a yellow dog'

token=nltk.word_tokenize(sentence)


tagged=nltk.pos_tag(token)
entities=nltk.chunk.ne_chunk(tagged)
chunker=RegexpParser("""
                       NP: {<DT>?<JJ>*<NN>}  
                       P: {<IN>}             
                       V: {<V.*>}              
                       PP: {<p> <NP>}         
                       VP: {<V> <NP|PP>*}      
                       """)
output=chunker.parse(tagged)
output.draw()
print(tagged)
print(entities)
t = nltk.corpus.treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()