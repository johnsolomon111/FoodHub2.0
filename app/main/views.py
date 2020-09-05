from flask import Blueprint, render_template, url_for, session, redirect

from app.services import login_user, auth_user
from app.main.forms import LoginForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('index.html', title="Welcome")

@main.route('/sign-in', methods=['GET','POST'])
def sign_in():
  form = LoginForm()
  message = ""
  if form.validate_on_submit():
    data = {
      'email' : form.email.data,
      'password' : form.password.data
    }
    user = login_user(data)
    if user['status'] == "success":
      get_user = auth_user(user['Authorization'])
      if get_user['data']['user_type'] == 'Owner':
        session['user'] = get_user['data']
        return redirect(url_for('owner.dashboard'))
      else:
        session['user'] = get_user['data']
        return redirect(url_for('customer.dashboard'))
    else:
      message = "Invalid Password/Email! Please try again."
      return render_template('login.html', form=form, title="Login", message=message)
  return render_template('login.html',form=form, title="Login")