import spacy

from spacy import displacy

nlp=spacy.load("en_core_web_sm")

text='''Python is an interpreted, high-level and general-purpose programming language,
       Pythons design philosophy emphasizes code readability with ,
       its notable use of significant indentation.
       Its language constructs and object-oriented approach aim to
       help programmers write clear and
       logical code for small and large-scale projects'''


doc=nlp(text)

sentences=list(doc.sents)
print(sentences)

for token in doc:
    print(token.text)

ents=[(e.text,e.start_char,e.end_char,e.label_) for e in doc.ents]
print(ents)
#displacy.render(doc,style='ent',jupyter=True)
