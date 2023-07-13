def equalStacks(a,b,c):
    x,y,z=map(sum,(a,b,c))
    while a and b and c:
        v=min(x,y,z)
        while x>v: x-=a.pop()        
        while y>v: y-=b.pop()        
        while z>v: z-=c.pop()
        if x==y==z: break
    return sum(a)
if __name__=="__main__":
    s=[]
    for i in range(0,3):
        a=input(f'Enter Stack {i+1} ')
        l=list(map(int,a.split(' ')))
        l.reverse()
        s.append(l)
    print(equalStacks(s[0],s[1],s[2]))