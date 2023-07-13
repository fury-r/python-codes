def combineParts(parts): #iterative_approach
    p1=0
    if(len(parts))==1:return 0
    i=1
    while True:
        print(i)
        parts.sort()
        print(parts)
        if(len(parts)==2):
                return p1+sum(parts)
        p=parts.pop(0)+parts.pop(0)
        p1+=p
        parts.append(p)
        print(p,parts)
        i+=1
print(combineParts([8,4,6,12])) 
def combineParts(parts):#recursive_approach
    parts.sort()
    if(len(parts)==2):
        return sum(parts)
    p=parts.pop(0)+parts.pop(0)
    parts.append(p)
    return p+combineParts(parts)










# I have used the iterative Approach for solving this i have used a while true loop   then i m sorting the list in increasing order

# then i have a  if conditions which will break the loop if the a condition is met

# my variable 'p' hold the sum of the popped first two elements then i am adding it to a temporary variable 'p1' and then  appending 'p' it to the list.

# Then this will loop run keep until the length of the list is equal to 2  when it meets the condition it'll  return p1 which was my temporary variable it'll add it to the the sum of main list which only has two elements and return the value.


# The time complexity is O(n)
