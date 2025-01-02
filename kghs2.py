from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    html = '<img src="https://uniform.wingzero.tw/assets/images/badge/tw-kaohsiung-kghs.jpg">\n'
    html += "Hello, <font color=magenta>kghs</FONT>\n"
    return html
