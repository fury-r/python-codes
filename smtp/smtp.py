import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
l=['jack','john','']
html=Template(Path("index.html").read_text())
email=EmailMessage() #for email body
email['from']='Test123'
email["to"]="RECEIPENT EMAIL"
email['subject']="Jod email"
email.set_content("I am JOD")
email1=EmailMessage()
email1['from']='Test123'
email1["to"]="receipent email"
email1['subject']="Jod email"
for i in l:
    email1.set_content(html.substitute(name=i),'html') #html sets html  ,by default texts
    with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp: #for smtp 
        smtp.ehlo()
        smtp.starttls()
        smtp.login("YOUR EMAIL","pASSWORD")
        smtp.send_message(email)
        smtp.send_message(email1)

        print("Done!")
