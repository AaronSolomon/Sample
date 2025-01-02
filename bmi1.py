from flask import Flask, request
app = Flask(__name__)

@app.route('/form')
def form():
    html = """<form action='/bmi'>
    <input type=text name=height><br>
    <input type=text name=weight><br>
    <input type=submit>"""
    return html

@app.route('/bmi')
def bmi():
    return str(request.values)

