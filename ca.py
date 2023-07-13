a=int(input("Enter a  Number "))
b,n=1,a-1
q='5'
for i in range(1,a+1):
    b=b*i
    q+='*'+str(n)
    n-=1
q=q[:-2]
print(q+"="+str(b))