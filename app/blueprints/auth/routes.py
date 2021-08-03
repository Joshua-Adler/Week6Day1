from flask import render_template, flash, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from . import bp as auth
from .forms import LoginForm, RegisterForm, EditProfileForm
from .models import User

@auth.route('/logout')
@login_required
def logout():
	if current_user:
		logout_user()
		flash('Logged out', 'warning')
		return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST' and form.validate_on_submit():
		email = form.email.data.lower()
		password = form.password.data
		user = User.query.filter_by(email=email).first()
		if user and user.check_hashed_password(password):
			login_user(user)
			flash('Logged in', 'success')
			return redirect(url_for('main.index'))
		else:
			flash('Email or password incorrect', 'danger')
			return redirect(url_for('auth.login'))
	return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if request.method == 'POST' and form.validate_on_submit():
		try:
			data = {
				'first': form.first.data.title(),
				'last': form.last.data.title(),
				'email': form.email.data.lower(),
				'password': form.password.data,
			}
			user = User()
			user.from_dict(data)
		except:
			flash('Error: there was an error. Please try not to do that.', 'danger')
			return render_template('auth/register.html', form=form)
		flash('Registration successful', 'success')
	return render_template('auth/register.html', form=form)

@auth.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
	form = EditProfileForm()
	if request.method == 'POST' and form.validate_on_submit():
		#try:
			data = {
				'first': form.first.data.title(),
				'last': form.last.data.title(),
				'email': form.email.data.lower(),
				'password': form.password.data,
			}
			user = User.query.filter_by(email=form.email.data.lower()).first()
			print(user.email, current_user.email)
			if user and current_user.email != user.email:
				flash('Email already in use', 'danger')
				return redirect(url_for('auth.edit_profile'))

			current_user.from_dict(data)
			flash('Profile Updated', 'success')
			return redirect(url_for('main.index'))
		#except:
			#flash('Unexpected error', 'danger')
			#return redirect(url_for('auth.edit_profile'))

	return render_template('auth/register.html', form=form)