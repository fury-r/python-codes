def gradingStudents(grades):
    q=[i+(5*round(i/5)-i)  if(i>35 and (5*round(i/5)-i)>0 and(5*round(i/5)-i)<3) else i for i in grades]
    return q
print(gradingStudents([73,67,38,33]))