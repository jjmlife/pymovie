# coding:utf8
from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home
from app.admin import admin

app.register_blueprint(home)
app.register_blueprint(admin, url_prefix="/admin")
