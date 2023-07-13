import sys
def floydWarshall(arr):
    for x in range(len(arr)):
        for i in range(len(arr)):
            if x!=i:
                for j in range(len(arr)):
                    if j!=x:
                        arr[i][j]= min(arr[i][j],arr[i][x]+arr[x][j]) 
        

    print(arr)
infinity=sys.maxsize

arr=[
[0,3,infinity,7],
[8,0,2,infinity],
[5,infinity,0,1],
[2,infinity,infinity,0]
]

arr1=[
[0,8,infinity,1],
[infinity,0,1,infinity],
[4,infinity,0,infinity],
[infinity,2,9,0]
]
floydWarshall(arr)