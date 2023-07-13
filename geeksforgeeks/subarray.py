def subArraySum(arr,n,s):
    for i in range(n):
        j=i+1
        current=arr[i]
        while j<=n:
            print(i,j,sum(arr[i-1:j+1]))
            if current==s:
                return i+1,j
            current=sum(arr[i-1:j+1])
            j+=1
    return -1
x=list(map(int,"142 112 54 69 148 45 63 158 38 60 124 142 130 179 117 36 191 43 89 107 41 143 65 49 47 6 91 130 171 151 7 102 194 149 30 24 85 155 157 41 167 177 132 109 145 40 27 124 138 139 119 83 130 142 34 116 40 59 105 131 178 107 74 187 22 146 125 73 71 30 178 174 98 113".split(" ")))
print(subArraySum(x,len(x),665))