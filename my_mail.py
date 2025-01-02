from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    if 'mail' in request.values:
        return "{}<br> {}<br> {}".format(request.values['mail'],
                request.values['homepage'], request.values['time'])
    else:
        return '''<form>
  <input type="email" name="mail"><br>
  <input type="url" name="homepage"><br>
  <input type="time" name="time"><br>
  <input type="submit">
</form>'''


