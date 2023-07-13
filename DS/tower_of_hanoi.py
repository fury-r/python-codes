def tower_of_hanoi_recursive(n,a,b,c):
    if(n>0):
        tower_of_hanoi_recursive(n-1,a,c,b)
        print(f"{a} to {c}")
        tower_of_hanoi_recursive(n-1,b,a,c)
    return 0
def tower_of_hanoi_iterative(n,a,b,c):
    m=pow(2,n)-1
    for i in range(1,m+1):
        if(i%3==1):
            print(a,c)
        elif(i%3==2):
            print(a,b)
        elif(i%3==0):
            print(c,b)
    return 0

print(tower_of_hanoi_recursive(3,"A","B","C"))
print(tower_of_hanoi_iterative(3,"A","B","C"))

