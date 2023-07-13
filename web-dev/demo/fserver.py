from flask import Flask,render_template,request,redirect
from flask.helpers import url_for
import csv
app=Flask(__name__)

@app.route('/')
def home():
    return render_template(f"index.html")

@app.route('/<string:page_name>')
def pages(page_name="/"):
    if(page_name=='/'):
        return render_template(f"index.html")
    else:
        return render_template(f"{page_name}.html")

def write_to_csv(data):
    fs=open("./database.csv",'a' ,newline='')
    csv_writer=csv.writer(fs,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([data['email'],data['subject'],data['message']])
    return 0
@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    error = None
    if request.method == 'POST':
        try:
            data=request.form.to_dict()
            print(data)
            write_to_csv(data)
        except:
            return "Something went wrong"
        # fs=open('./database.txt','a')
        # fs.write(f"\nEmail:{data['email']}\nSubject{data['subject']}\nBody:{data['message']}\n")            
        # fs.close()
        return redirect('/thankyou')
    else:
        return "something went wrong"

