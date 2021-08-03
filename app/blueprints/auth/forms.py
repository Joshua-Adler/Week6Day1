from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from .models import User

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[Email(), DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
	first = StringField('First Name', validators=[DataRequired()])
	last = StringField('Last Name', validators=[DataRequired()])
	email = StringField('Email', validators=[Email(), DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	conf_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Submit')

	def validate_email(form, field):
		user = User.query.filter_by(email=field.data).first()
		if user:
			raise ValidationError('Email already in use.')

class EditProfileForm(FlaskForm):
	first = StringField('First Name', validators=[DataRequired()])
	last = StringField('Last Name', validators=[DataRequired()])
	email = StringField('Email Address', validators=[Email(), DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	conf_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Submit')