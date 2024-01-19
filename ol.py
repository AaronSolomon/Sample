from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    html = '''<h1>Ordered List and Unordered Lists</h1>
    <h2>Ordered List</h2>
    <ol>
    <li>One</li>
    <li>Two</li>
    <li>Three</li>
    </ol>

    <h2>Unordered List</h2>
    <ul>
    <li>One</li>
    <li>Two</li>
    <li>Three</li>
    </ul>'''
    return html
