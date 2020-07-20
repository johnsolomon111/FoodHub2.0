from flask import Flask, render_template, url_for, redirect, jsonify, request, make_response, session

server = Flask(__name__)
server.config['SECRET_KEY'] = 'secretsecretsecret'

from app.views import *
