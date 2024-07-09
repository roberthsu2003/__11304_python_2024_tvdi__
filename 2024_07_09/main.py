from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>我的主題</h1>\n<h2>職能發展學院</h2>"

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