from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_page():
    return('<p>Index page. Flask!</p>')

@app.route('/hello')
def hello_world():
    return('<p>Hello world!</p>')
