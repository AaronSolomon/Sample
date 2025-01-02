from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def select():
    if request.method == 'GET':
        html = '''<form method=post>
  <input type="checkbox" name="bike"  value="Bike">
  I have a bike<br>
  <input type="checkbox" name="car"  value="Car">
  I have a car<br>
  <input type="checkbox" name="boat"  value="Boat">
  I have a boat<br>
  <input type="submit">
</form> '''
        return html
    else:   # POST
        v = []
        for name in ['bike', 'car', 'boat']:
            value = request.values.get(name)
            if value:   # If the item is not checked, value will be None
                v.append(value)

        return 'You have ' + ','.join(v)

