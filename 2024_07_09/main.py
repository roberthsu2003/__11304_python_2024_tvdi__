from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
<<<<<<< HEAD
def hello_world():
    return "<h1>Hello, World!</h1>"
=======
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return '<h1>Hello, World</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    return f"<h1>Hello! {username}</h1>"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'<h1>Post {post_id}</h1>'
>>>>>>> c24c6e4a7b6d37e99bb3b7838b6985d0e094293f
