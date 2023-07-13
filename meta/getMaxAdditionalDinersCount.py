from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S=sorted(S)
    count=0
    head=-K
    tail=0
    flag=0
    for i in range(0,N):
        
        if i>head:
            if flag==0 and i<S[tail]-K-1:
                count+=1
                print("previous at",head," sit at",i," next is",S[tail],"gap is ",K,S[tail-1])
                head=i+K

            elif flag==1:
                count+=1
                print("previous at",head," sit at",i," gap is ",K)
                head=i+K
        if flag==0 and i+1>S[tail]:
            tail+=1
            head=S[tail-1]+K-1
            if tail==len(S):
                flag=1
        
    return count

print(getMaxAdditionalDinersCount(10,1,2,[2,6,]))

print(getMaxAdditionalDinersCount(15,2,3,[11,6,14]))

