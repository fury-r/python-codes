import spacy
nlp=spacy.load('en_core_web_sm')


text='''Python is an interpreted, high-level and general-purpose programming language,
       Pythons design philosophy emphasizes code readability with ,
       its notable use of significant indentation.
       Its language constructs and object-oriented approach aim to
       help programmers write clear and
       logical code for small and large-scale projects'''

doc=nlp(text)
sentence=doc.sents
print(list(sentence))
print(doc.ents)
x=[(e.text,e.label_) for e in doc.ents]
print(x)