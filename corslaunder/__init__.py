# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/get/*": {"origins": "*"}})

from . import views
