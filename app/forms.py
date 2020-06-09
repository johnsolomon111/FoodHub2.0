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
	start_sun = StringField('start_sun')
	start_mon = StringField('start_mon')
	start_tue = StringField('start_tue')
	start_wed = StringField('start_wed')
	start_thu = StringField('start_thu')
	start_fri = StringField('start_fri')
	start_sat = StringField('start_sat')
	end_sun = StringField('end_sun')
	end_mon = StringField('end_mon')
	end_tue = StringField('end_tue')
	end_wed = StringField('end_wed')
	end_thu = StringField('end_thu')
	end_fri = StringField('end_fri')
	end_sat = StringField('end_sat')