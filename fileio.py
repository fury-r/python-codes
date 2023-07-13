c=open('test.txt')
print(c.read())
c.seek(0) #moving the cursor to a desired location
print(c.read())
print(c.readline()) #reading one line
print(c.readlines()) #reading all lines


c.close()