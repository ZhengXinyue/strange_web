from flask import Flask

# https://greyli.com/
# https://flask.net.cn/quickstart.html#id2

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'home page'


@app.route('/posts')
def show_posts_list():
    return 'posts page'


@app.route('/')
def show_post():
    pass
