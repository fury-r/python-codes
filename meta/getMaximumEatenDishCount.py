from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  eaten=[]
  count=0
  for i in range(N):

    if  D[i] not in eaten:
        eaten.append(D[i])
        count+=1
        if len(eaten)>K:
          eaten.pop(0)
  return count

  # eaten=[]
  # count=0
  # for i in range(N):

  #   if  D[i] not in eaten[count-K:count]:
  #       eaten.append(D[i])
  #       count+=1
     
    
  # return count

print(getMaximumEatenDishCount(6,[1, 2, 3, 3, 2, 1],1))
print(getMaximumEatenDishCount(6,[1, 2, 3, 3, 2, 1],2))
print(getMaximumEatenDishCount(7,[1, 2, 1, 2, 1, 2, 1],2))