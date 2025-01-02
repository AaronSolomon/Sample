from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def select():
    if request.method == 'GET':
        html = '''<form method=post>
  <input type="checkbox" name="vehicle"  value="Bike">
  I have a bike<br>
  <input type="checkbox" name="vehicle"  value="Car">
  I have a car<br>
  <input type="checkbox" name="vehicle"  value="Boat">
  I have a boat<br>
  <input type="submit">
</form> '''
        return html
    else:   # POST
        v = request.values.getlist('vehicle')
        return 'You have ' + ','.join(v)

