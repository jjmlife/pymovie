# coding:utf8
from flask import Blueprint

home = Blueprint("admin", __name__)

import app.admin.views
