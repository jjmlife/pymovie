# coding:utf8
from . import home


@home.route("/")
def index():
    return "<h1 style='color:red'> admin </h1>"
