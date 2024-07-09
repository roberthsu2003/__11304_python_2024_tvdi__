from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>我的主題</h1>\n<h2>職能發展學院</h2>"

@app.route('/hello')
def hello():
    return '<h1>Hello, World</h1>'