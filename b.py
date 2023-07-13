#user_name=input("Enter the username ")
#password=input("Enter the password ")
#print(f"{user_name} your password {len(password)*'*'} is {len(password)} letters long ")

#a='*'
#for i in  range(10,0,-1):
#        print(a*i)

a=['a','a','b','c','d','d','e','f','g','g','h','i','i']
l=[]
for i in  (a):
    if(a.count(i)>1):
        if i not in l:
         l.append(i)
print(l)

def test(a):
        '''
        Info: This function takes a variable and prints it
        '''
        print(a)
test(2222)