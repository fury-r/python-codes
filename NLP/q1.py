import re

pattern=re.compile(r'[$]\w*[0-9](\.)?[0-9]{0,2}|[0-9]*(\.)[0-9]{0,2}[$]|\b\w*[0-9][Gg]\w*\w*[Bb]\w*\b|\b\w*[0-9][Gg]\w*[Hh]\w*[Zz]\w*\b|(\w+[(\.)])+\w')

text='I want to buy a PC with 500GB Harddisk 6Ghz CPU and below $999.99999 100.00$  from U.S.A.'

p=pattern.finditer(text)
l=[]
for i in p:
    l.append(i.group())
print(l)

#\b[0-9][Gg]\w*[Hh]\w*[Zz]\b|\$\d*\.?\d{0,2}\$?|\d*\.?\d{0,2}\$|\b[Tt]he\b|\b[Tt]hey\b