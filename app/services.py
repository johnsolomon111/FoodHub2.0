import requests
from flask import jsonify

url = 'http://127.0.0.1:8080/'

def add_new_user(data):
	req = str(url) + 'user/'
	r = requests.post(req, json=data)
	res = r.json()
	return res

def auth_user(token):
	headers = {'Authorization' : token}
	req = str(url) + 'auth/authorize_user'
	new_r = requests.post(req, headers=headers)
	return new_r.json()

def login_user(data):
	req = str(url) + 'auth/login'
	r = requests.post(req, json=data)
	res = r.json()
	return res

def get_all_resto(user_id):
	req = str(url) + 'restaurant/' + str(user_id)
	r = requests.get(req)
	res = r.json()
	return res['data']

def add_new_resto(data, user_id):
	req = str(url) + 'restaurant/' + str(user_id)
	r = requests.post(req, json=data)
	res = r.json()
	return res	