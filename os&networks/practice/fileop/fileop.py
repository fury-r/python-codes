import os,shutil


fs=open('a.txt','w+')
fs.write(input('Text: '))
fs.seek(int(input('pointer: ')))
print(fs.read())
fs.close()
print('size',os.stat(input('filename')).st_size)
a=os.open(input('filename: '),os.O_RDWR|os.O_CREAT)
dp=os.dup(a)
print(f'Descriptor {dp}')
p=dp
z=str.encode(str(p))
os.write(dp,z)
os.closerange(a,dp)

if(os.link(input('First File: '),input('Second File: ')))==-1: print('File Already Link')

os.unlink(input('Second File: '))
fs=open(input('File: '),'wb')
fs.seek(4000-1)
fs.write(b'/b')
shutil.copy(input('source: '),input('destination: '))
a=os.listdir()
print(a)