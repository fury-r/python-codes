import sys

def bellmanFord(arr,source):
    final_arr=[arr[source][i] for i in range(0,len(arr))]
    print(final_arr)
    for k in range(1,len(arr)):
        for j in range(0,len(arr)):
            if source!=j:
                minimun=[final_arr[j]]+[final_arr[x]+arr[x][j] for x in range(0,len(arr)) if x!=source and x!=k]
                final_arr[j]=min(minimun)
    print(final_arr)

infinity=sys.maxsize
arr=[
[0,4,6,infinity,infinity,],
[infinity,0,8,-3,infinity,],
[infinity,infinity,0,-2,11],
[infinity,infinity,infinity,0,infinity],
[2,infinity,infinity,8,0]
]
bellmanFord(arr,0)