from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    html = "Hello, Flask"
    return html

@app.route('/<name>')
def hello(name):
    return "Hello, " + name

@app.route('/weekday/<year>/<month>/<day>')
def weekday(year, month, day):
    return "{:04}-{:02}-{:02}".format(int(year), int(month), int(day))

@app.route('/now')
def now():
    from datetime import datetime
    t = datetime.now()
    html = "Now is {}:{:02}".format(t.hour, t.minute)
    if t.hour < 12:
        html += '<br>Good morning.'
    elif t.hour < 18:
        html += '<br>Good afternoon.'
    else:
        html += '<br>Good evening.'
    return html

