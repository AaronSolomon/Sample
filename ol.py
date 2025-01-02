from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    items = ['One', 'Two', 'Three']
    html = '''<h1>Ordered List and Unordered Lists</h1>
    <h2>Ordered List</h2>
    <ol>\n'''
    for item in items:
        html += '<li>' + item + '</li>\n'
    html += '''</ol>

    <h2>Unordered List</h2>
    <ul>\n'''
    for item in items:
        html += '<li>' + item + '</li>\n'
    html += '</ul>'
    return html
