from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html.jinja')

@app.route('/new')
def new():
    return render_template('new.html.jinja')

@app.route('/youbike')
def youbike():
    return render_template('youbike.html.jinja')

@app.route('/contact')
def contact():
    # show the post with the given id, the id is an integer
    return render_template('contact.html.jinja')