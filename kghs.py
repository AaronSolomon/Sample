from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''This is a longer article.
    In Python, you use 3 quotation marks for multi-line strings.
    Your browser will re-arrange the text automatically, when you
    resize the browser window.
    Here is a hyperlink to
    <a href="https://cnn.com/">CNN</a>.'''
