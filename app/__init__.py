from flask import Flask, render_template, url_for

server = Flask(__name__)

from app.views import *
