def birthday(s,d,m):
    return len([1 for i in range(((len(s)-m)+1)) if sum(s[i:i+m])==d])

print(birthday([1,2,1,3,2],3,2))