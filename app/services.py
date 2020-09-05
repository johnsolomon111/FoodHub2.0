import requests
from flask import jsonify

url = 'http://localhost:8080/api/v1/'

def create_user(data):
	req = str(url) + 'user/sign-up'
	r = requests.post(req, json=data)
	res = r.json()
	return res

def auth_user(token):
	headers = {'Authorization': token}
	req = str(url) + 'auth/user'
	new_r = requests.post(req, headers=headers)
	return new_r.json()

def login_user(data):
	req = str(url) + 'auth/login'
	r = requests.post(req, json=data)
	res = r.json()
	return res

def auth_customer(token):
  headers = {'Authorization' : token}
  req = str(url) + 'auth/authorize_customer'
  new_r = requests.post(req, headers=headers)
  return new_r.json()

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