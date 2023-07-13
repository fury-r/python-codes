import re

val=re.compile(r' ([a-zA-Z]).([a])')
#wage=df1['Wage'].replace('[\€]','',regex=True) regex with replace

string ="hello World"
a=re.search("hello",string)
print(a)
print(a.span())
print(a.group)
q=re.compile("hello")
string2 ="hello how are you"

b=q.search(string2)
print(b)
print(b.span())
print(b.group)
v=val.search(string2)
print(f"{v} ggg")

d=q.findall(string)

e=q.fullmatch(string)
f=q.match(string)

print(f"{d} d" )
print(f"{e} e")
print(f"{f} f")
 

 ##use for password checking