def check_if_palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
def check_if_num_palindrome(a):
    n=a
    s=0
    while n>0:
        r=n%10
        s=r+(s*10)
        n=n/10
    print(s,a)
    if(s==a):
        return True
    return False
print(check_if_palindrome("nitin"))

print(check_if_num_palindrome(2002))