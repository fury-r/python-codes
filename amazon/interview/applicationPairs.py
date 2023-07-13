def applicationPairs(deviceCapacity, foregroundAppList, backgroundAppList):
    l=[[i[1]+j[1],i[0],j[0]] for  i in foregroundAppList for j in backgroundAppList if i[1]+j[1]<=deviceCapacity]
    l.sort() 
    q=[[i[1],i[2],i[0]] for  i in l if i[0]<deviceCapacity]
    c=[[i[1],i[2]] for i in l if(i[0]==deviceCapacity)]
    x=[]
    if len(c)==0 and len(q)==0:
        return [{}]
    if len(c)==0:

        while True:            
            deviceCapacity-=1
            for i in q:
                if(deviceCapacity==i[2]):
                    x.append([i[0],i[1]])
            if len(x)>0:
                return x
    return c
print(applicationPairs(7,[[1,1],[2,4],[3,6]],[[1,2]]))
# i have first checked for the first condition which is to check if a combination usage is less than deviceCapacity i have checked for it and stored in an array then i have seperated the elements in two more lists one which checks for less then deviceCapacity which is 'q' and the other one is equal to the deviceCapacity  which is variable 'c' then i set a condition to check if the first array which is c if its length is 0 that mean no combination memory requirement equals the deviceCapacity  so i have used a  loop to print the next  optimal combination

# the while loop in the begining will subtract for one from deviceCapacity  because we are checking for the next optimal solution then in the for loop the give condition will check if  the combination value equals new deviceCapacity  value this loop will break only if length of 'list is greater than 0  or else it'll subtract one for deviceCapacity  and it'll check again until my 'x' list has length greater then 0 itll return 'x' list

# .The 'x' list is used to store the pairs which meet the condition of the if loop in the for loop

# if my 'c' list has length greater then 0 then it'll return the C list .


# The Time Complexity is O(n)