from flask import Flask
app = Flask(__name__)

@app.route('/weekday/<year>/<month>/<day>')
def weekday(year, month, day):
    return "{}-{}-{}".format(year, month, day)
