from flask import Flask, request
app = Flask(__name__)

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

