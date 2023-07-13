from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  result=sum([ len([1 for j in i if j==1 ]) for i in G])/(R*C)
  return result
