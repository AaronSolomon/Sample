from flask import Flask
app = Flask(__name__)	# double underline

@app.route('/')
def index():
    return "Hello, Flask\n"
