def jumpingOnClouds(c):
    if len(c) == 1 : return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    if c[2]==1:
        print(c[1:]) 
        return 1 + jumpingOnClouds(c[1:])
    if c[2]==0:
        print(c[2:]) 

        return 1 + jumpingOnClouds(c[2:])

print(jumpingOnClouds([0, 0, 0, 1 ,0 ,0]))
print(jumpingOnClouds([0, 0, 1, 0 ,0,1 ,0]))

