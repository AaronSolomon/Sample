from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def select():
    if request.method == 'GET':
        html = '''<form method=post>
  <input type="radio" name="fav_language"  value="html">
  HTML<br>
  <input type="radio" name="fav_language"  value="css">
  CSS<br>
  <input type="radio" name="fav_language"  value="js">
  JavaScript<br>

  <input type=submit>
</form> '''
        return html
    else:   # POST
        value = request.values.get('fav_language')
        if not value:   # If the item is not checked, value will be None
            value = 'Nothing'

    return 'You choose ' + value

