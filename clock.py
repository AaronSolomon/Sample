from flask import Flask
app = Flask(__name__)

@app.route('/now')
def now():
    from datetime import datetime
    t = datetime.now()
    html = "Now is {}:{}".format(t.hour, t.minute)
    if t.hour < 12:
        html += '<br>Good morning.'
    elif t.hour < 18:
        html += '<br>Good afternoon.'
    else:
        html += '<br>Good evening.'
    return html
