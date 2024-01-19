from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask\n“
@app.route('/morning')
def morning():
    return "Good morning!\n"
