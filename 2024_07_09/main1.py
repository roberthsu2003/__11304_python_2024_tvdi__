from flask import Flask,url_for

app = Flask(__name__)
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login abc'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', name='robert', password='1234'))
    print(url_for('profile', username='John Doe'))