from flask import request, render_template, Flask
import re

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    new = ''
    if request.method == 'POST':
        input_text = request.form.get('text')
        input_pattern = request.form.get('pattern')
        match = re.findall(input_pattern,input_text)
        print(match)
        if match:
            return render_template('home.html', k=match, t=input_text)

    return render_template('home.html')

def checkmail(m):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, m):
        return "Valid Email"
    else:
        return "Invalid Email"

@app.route('/emailvalidation', methods=['POST','GET'])
def email():
    if request.method == 'POST':
        mail = request.form.get('email')
        result = checkmail(mail)
        return render_template('email.html',r=result)
    else:
        return render_template('email.html')


app.run(host='0.0.0.0',port=5000,debug=True)