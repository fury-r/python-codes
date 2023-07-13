def timeConversion(s):
    if('PM' in s and  '12' not in s ):
        l=12+int(s[:2])
        a=s.replace(s[:2],str(l))
        a=a.rstrip(s[-2:])
        return a
    elif('12' in s and 'AM' in s):
        a=s.replace(s[:2],str('00'))
        a=a.rstrip(s[-2:])
        return a
    else :return s.rstrip(s[-2:])

print(timeConversion('12:45:54PM'))