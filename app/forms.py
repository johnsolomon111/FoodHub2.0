from flask_wtf import FlaskForm, Form 
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired()])
	phone_number = StringField('phone_number', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])

class LoginForm(FlaskForm):
	email = StringField('email', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])

class RestaurantForm(FlaskForm):
	resto_name = StringField('resto_name')
	location = StringField('location')
	resto_description = TextAreaField('resto_description')
	services = StringField('services')
	start_weekend = StringField('start_weekend')
	start_weekday = StringField('start_weekday')
	end_weekend = StringField('end_weekend')
	end_weekday = StringField('end_weekday')