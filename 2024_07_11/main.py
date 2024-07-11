from flask import Flask,render_template
import data

app = Flask(__name__)
@app.route("/")
def index():
    print(data.get_areas())
    return render_template('index.html.jinja')