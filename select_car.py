from flask import Flask, request
app = Flask(__name__)

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

