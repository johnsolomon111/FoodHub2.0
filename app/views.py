from app import *
from app.forms import RegistrationForm, LoginForm, RestaurantForm
from app.services import add_new_user, auth_user, login_user, get_all_resto, add_new_resto
from functools import wraps

global_token = ''

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		global global_token
		print(global_token)
		token = global_token
		get_user = auth_user(token)
		if not get_user:
			return jsonify({'message':'token missing'})
		else:
			return f(get_user, *args, **kwargs)
	return decorated

@server.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html', title="Welcome to FoodHub :)")

@server.route('/login/owner', methods=['GET','POST'])
def login_owner():
	form = LoginForm()
	message = ''
	if form.validate_on_submit():
		data = {
			'email' : form.email.data,
			'password' : form.password.data
		}
		user = login_user(data)
		if user['status'] == 'success':
			global global_token
			global_token = user['Authorization']
			print(global_token)
			return redirect(url_for('restaurant'))
		else:
			message = 'Invalid Password/Email, please try again'
			return render_template('login/login_owner.html', title='Login as Owner', form=form, message=message)
	return render_template('login/login_owner.html', title="Login as Owner", form=form, message=message)

@server.route('/login/customer', methods=['GET','POST'])
def login_customer():
	return render_template('login/login_customer.html', title="Login as Customer")

@server.route('/signup', methods=['GET','POST'])
def signup():
	form = RegistrationForm()
	message = ''
	if form.validate_on_submit():
		data = {
			'email' : form.email.data,
			'name' : form.name.data,
			'phone_number' : form.phone_number.data,
			'password' : form.password.data
		}
		new_user = add_new_user(data)
		if new_user["status"] == "success":
			global global_token
			global_token = new_user["Authorization"]
			return redirect(url_for('restaurant'))
		else:
			message = 'Email already exists'
			return render_template('signup/signup.html', title="Sign up for FoodHub", form=form, message=message)
	return render_template('signup/signup.html', title="Sign up for FoodHub", form=form, message=message)



@server.route('/restaurant', methods=["GET", "POST"])
@token_required
def restaurant(get_user):
	if get_user['status'] == 'fail':
		form = LoginForm()
		message = 'Session Expired, please login again'
		return render_template('login/login_owner.html', title='Login as Owner', form=form, message=message)
	else:
		data = get_user['data']
		print(get_user)
		restos = get_all_resto(data['user_id'])
		print(restos[0]['resto_name'])
		resto_data = restos[0]
	
	return render_template('dashboard/restaurant.html',data=data, resto=resto_data, restos=restos, title='Restaurant Page')

@server.route('/restaurant/add', methods=['GET','POST'])
@token_required
def add_restaurant(get_user):
	global global_token
	message = ''
	form = RestaurantForm()
	print(global_token)
	print(get_user)
	user_id = get_user['data']['user_id']
	if form.validate_on_submit():
		data = {
			'resto_name' : form.resto_name.data,
			'location' : form.location.data,
			'resto_description' : form.resto_description.data,
			'services' : form.services.data,
			'sun' : form.start_sun.data + ' - ' +form.end_sun.data,
			'mon' : form.start_mon.data + ' - ' +form.end_mon.data,
			'tue' : form.start_tue.data + ' - ' +form.end_tue.data,
			'wed' : form.start_wed.data + ' - ' +form.end_wed.data,
			'thu' : form.start_thu.data + ' - ' +form.end_thu.data,
			'fri' : form.start_fri.data + ' - ' +form.end_fri.data,
			'sat' : form.start_sat.data + ' - ' +form.end_sat.data
		}
		new_resto = add_new_resto(data,user_id)
		if new_resto['status'] == 'success':
			return redirect(url_for('restaurant'))
		else:
			message = 'Restaurant name already Exits'
			return render_template('dashboard/add_restaurant.html',title='Add Restaurant',form=form, message=message)
	return render_template('dashboard/add_restaurant.html',title='Add Restaurant',form=form, message=message)
