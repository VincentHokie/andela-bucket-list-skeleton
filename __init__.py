__author__ = 'MacUser'

from flask import Flask

app = Flask(__name__)

from . import views


