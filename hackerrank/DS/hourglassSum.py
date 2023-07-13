import abc


def hourglassSum(arr):
    sum= [arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2] for i in range(len(arr)-2) for j in range((len(arr)-2))]
    return max(sum)
print([[1,0,5],[1,1,7],])

""" 6x6 matrix
abc
 d
efg """