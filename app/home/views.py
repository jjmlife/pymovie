# coding:utf8
from . import home


@home.route("/")
def index():
    return "<h1 style='color:blue'> home </h1>"
