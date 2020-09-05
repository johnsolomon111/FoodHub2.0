from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
  full_name = StringField('full_name', validators=[DataRequired()])
  email = EmailField('email', validators=[DataRequired()])
  phone_number = StringField('phone_number', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])

class LoginForm(FlaskForm):
  email = EmailField('email', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])