from app import *

@server.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html', title="Welcome to FoodHub :)")

@server.route('/login/owner', methods=['GET','POST'])
def login_owner():
	return render_template('login/login_owner.html', title="Login as Owner")

@server.route('/login/customer', methods=['GET','POST'])
def login_customer():
	return render_template('login/login_customer.html', title="Login as Customer")

@server.route('/signup', methods=['GET','POST'])
def signup():
	return render_template('signup/signup.html', title="Sign up for FoodHub")