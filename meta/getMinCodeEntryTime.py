from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  ans=0
  pos=1
  clock=list(range(1,N))
  for i in C:
    print(pos-i,-pos-i,'from',pos,'to',i)
    if pos-i>i-pos:
      ans+=pos-i
      pos=clock[pos-i]
    else:
      ans+=i-pos
      pos=clock[i-pos]
  return ans

print(getMinCodeEntryTime(3,3,[1, 2, 3]))
print(getMinCodeEntryTime(10,4, [9, 4, 4, 8]))