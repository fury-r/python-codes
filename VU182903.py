def calc_grade(l):
    percentage=sum(l)
    percentage=(percentage*100)/300
    for i in (l):
        if(i>=95):
            print('Grade for '+str(i)+' subject:A+')
        elif(i>=90 and i<=94):
            print('Grade for '+str(i)+' subject:A')
        elif(i>=80 and i<=89):
            print('Grade for '+str(i)+' subject:B')
        elif(i>=70 and i<=79):
            print('Grade for '+str(i)+' subject:C')
        elif(i>=60 and i<=69):
            print('Grade for '+str(i)+' subject:D')
        elif(i>=40 and i<=59):
            print('Grade for '+str(i)+' subject:E')
        elif(i>=0 and i<=39):
            print('Grade for '+str(i)+' subject:F')
    print("Percentage: "+str(percentage))
    if(percentage>=95):
        print('Over all Grade: A+') 
    elif(percentage>=90 and percentage<=94):
        print('Over all Grade: A')
    elif(percentage>=80 and percentage<=89):
        print('Over all Grade: B')
    elif(percentage>=70 and percentage<=79):
        print('Over all Grade: C')
    elif(percentage>=60 and percentage<=69):
        print('Over all Grade: D')
    elif(percentage>=40 and percentage<=59):
        print('Over all Grade: E')
    else:
        print('Over all Grade: F')
        



l=[]
subj=0
for i in range(0,3):
        subj=int(input('Enter the marks for '+str(i+1)+' subject '))
        l.append(subj)
calc_grade(l)