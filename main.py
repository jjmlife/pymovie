# coding:utf8
from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return "<h1 style='color:red'>heloo world </h1>"


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
