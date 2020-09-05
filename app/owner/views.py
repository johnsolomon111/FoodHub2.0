from flask import Blueprint, render_template, url_for, session, redirect

from app.services import create_user, auth_user
from app.owner.forms import LoginForm, RegistrationForm

owner = Blueprint('owner', __name__)

@owner.route('/sign-up', methods=['GET','POST'])
def owner_sign_up():
	form = RegistrationForm()
	message = ''
	if form.validate_on_submit():
		data = {
			'email' : form.email.data,
			'full_name' : form.full_name.data,
			'contact_number' : form.phone_number.data,
			'password' : form.password.data,
			'user_type' : 'Owner'
		}
		new_user = create_user(data)
		if new_user['status'] == "success":
			get_user = auth_user(new_user['Authorization'])
			session['user'] = get_user['data']
			return redirect(url_for('owner.dashboard'))
		else:
			message = 'Email already exists'
			return render_template('owner/sign_up.html', title="Sign Up", form=form, message=message)
	return render_template('owner/sign_up.html', title="Sign Up", form=form, message=message)

@owner.route('/dashboard')
def dashboard():
	# if session['user'] is None:
	# 	form = LoginForm()
	# 	message = 'Session expired. Please sign in.'
	# 	return render_template('login.html', title="Login", message=message)
	# else:
	# 	owner = session['user']
	return render_template('owner/dashboard.html', title="Dashboard", owner=owner)

@owner.route('/add-restaurant')
def add_restaurant():
	return render_template('owner/add_restaurant.html', title="Create")