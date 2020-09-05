from flask import Blueprint, render_template, url_for, session, redirect

from app.services import create_user, auth_user
from app.customer.forms import LoginForm, RegistrationForm

customer = Blueprint('customer', __name__)

@customer.route('/sign-up', methods=['GET','POST'])
def customer_sign_up():
	form = RegistrationForm()
	message = ''
	if form.validate_on_submit():
		data = {
			'email' : form.email.data,
			'full_name' : form.full_name.data,
			'contact_number' : form.phone_number.data,
			'password' : form.password.data,
			'user_type' : 'Customer'
		}
		new_user = create_user(data)
		if new_user['status'] == "success":
			get_user = auth_user(new_user['Authorization'])
			session['user'] = get_user['data']
			return redirect(url_for('customer.dashboard'))
		else:
			message = 'Email already exists'
			return render_template('customer/sign_up.html', title="Sign Up", form=form, message=message)
	return render_template('customer/sign_up.html', title="Sign Up", form=form, message=message)

@customer.route('/dashboard')
def dashboard():
	return render_template('customer/dashboard.html', title="Dashboard")
