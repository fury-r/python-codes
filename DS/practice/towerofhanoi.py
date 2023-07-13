def tower_of_hanoi(n,a,b,c):
    if n:
        tower_of_hanoi(n-1,a,c,b)
        print(a,c)
        tower_of_hanoi(n-1,b,a,c)
tower_of_hanoi(20,'A','B','C')