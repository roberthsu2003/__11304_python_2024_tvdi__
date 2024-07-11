from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    content = 'Use our powerful <strong>mobile-first</strong> flexbox grid to build layouts of all shapes and sizes thanks to a twelve column system, six default responsive tiers, Sass variables and mixins, and dozens of predefined classes.'
    return render_template('index.html.jinja',left=content)