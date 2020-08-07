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
	return render_template('index.html', title="Welcome")

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
			get_user = auth_user(user['Authorization'])
			session['user'] = get_user['data']
			return redirect(url_for('restaurant'))
		else:
			message = 'Invalid Password/Email, please try again'
			return render_template('login/login_owner.html', title='Login', form=form, message=message)
	return render_template('login/login_owner.html', title="Login", form=form, message=message)

@server.route('/login/customer', methods=['GET','POST'])
def login_customer():
	return render_template('login/login_customer.html', title="Login")

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
			get_user = auth_user(new_user['Authorization'])
			session['user'] = get_user['data']
			return redirect(url_for('restaurant'))
		else:
			message = 'Email already exists'
			return render_template('signup/signup.html', title="Sign Up", form=form, message=message)
	return render_template('signup/signup.html', title="Sign Up", form=form, message=message)



@server.route('/restaurant', methods=["GET", "POST"])
def restaurant():
	if session['user'] == None:
		form = LoginForm()
		message = 'Session Expired, please login again'
		return render_template('login/login_owner.html', title='Login as Owner', form=form, message=message)
	else:
		data = session['user']
		restos = get_all_resto(data['user_id'])
		if restos:
			resto_data = restos[0]
		else:
			resto_data = []
	
	return render_template('dashboard/restaurant.html',data=data, resto=resto_data, restos=restos, title='Restaurant Page')

@server.route('/create/restaurant', methods=['GET', 'POST'])
def create_restaurant():
	if session['user'] == None:
		form = LoginForm()
		message = 'Session Expired, please login again'
		return render_template('login/login_owner.html', title='Login as Owner',form=form, message=message)
	else:
		data = session['user']
		form = RestaurantForm()
		user_id = data['user_id']
		if form.validate_on_submit():
			form_data = {
				'resto_name' : form.resto_name.data,
				'location' : form.location.data,
				'resto_description' : request.form.get('description'),
				'services' : form.services.data,
				'sun' : form.start_weekend.data + ' - ' + form.end_weekend.data,
				'sat' : form.start_weekend.data + ' - ' + form.end_weekend.data,
				'mon' : form.start_weekday.data + ' - ' + form.end_weekday.data,
				'tue' : form.start_weekday.data + ' - ' + form.end_weekday.data,
				'wed' : form.start_weekday.data + ' - ' + form.end_weekday.data,
				'thu' : form.start_weekday.data + ' - ' + form.end_weekday.data,
				'fri' : form.start_weekday.data + ' - ' + form.end_weekday.data
			}
			new_resto = add_new_resto(form_data, user_id)
			if new_resto['status'] == 'success':
				return redirect(url_for('restaurant'))
			else:
				message = 'Restaurant Name already Exists'
				return render_template('dashboard/add_restaurant.html', title='Add Restaurant',form=form, message=message)
		return render_template('dashboard/create.html',form=form, data=data, title='Create Restaurant', message='')


	

@server.route('/restaurant/add', methods=['GET','POST'])
def add_restaurant():
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

