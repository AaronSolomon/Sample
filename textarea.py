from flask import Flask, request
app = Flask(__name__)

@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == "GET":
        html = '''<form method="POST">
        <textarea name="students" rows=4 cols=50></textarea>
        <br><input type=submit> <input type=reset>'''
        return html
    else: # POST
        students = request.values['students'].split("\r\n")
        html = '<ol>\n'
        for line in students:
            html += '<li>' + line + '\n'
        html += '</ol>\n'
        return html

