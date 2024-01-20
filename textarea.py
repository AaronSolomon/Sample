from flask import Flask, request
app = Flask(__name__)

@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == "GET":
        html = '''<form method="POST">
        <textarea name="students" rows=4 cols=50></textarea>
        <br><input type=submit> <input type=reset>'''
        return html
    else: # POST
        students = request.values['students'].split("\r\n")
        html = '<ol>\n'
        for line in students:
            html += '<li>' + line + '\n'
        html += '</ol>\n'
        return html

@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'GET':
        html = '''<form method=post>
Choose a car:
<select name="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
<input type=submit></form>'''
        return html
    else:   # POST
        v = request.values['cars']
        return v

@app.route('/vehicle', methods=['GET', 'POST'])
def vehicle():
    if request.method == 'GET':
        html = '''<form method=post>
How do you go to school?
<select name="vehicle" multiple>
  <option value="bicycle">Bicycle</option>
  <option value="bus">Bus</option>
  <option value="car">Car</option>
  <option value="train">Train</option>
</select>
<input type=submit></form>'''
        return html
    else:   # POST
        v = request.values.getlist('vehicle')
        return 'You go to school by ' + ','.join(v)

