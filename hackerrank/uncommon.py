def get_uncommon(s1,s2):
    for i in s1:
        if i not in s2:print(i)
    for i in s2:
        if i not in s1:print(i)

get_uncommon('nitin','nikhil')