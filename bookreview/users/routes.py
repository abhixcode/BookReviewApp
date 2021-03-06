from flask import render_template, url_for, flash, redirect, request, Blueprint
from bookreview.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from bookreview.models import User, Readinglist
from bookreview import create_app,db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

users = Blueprint('users', __name__)

# User registration functionality using bcrypt hashing for password encryption
@users.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('readinglist.home',user_id=current_user.id))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email= form.email.data,password= hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template("register.html", form=form, title = "Register")

# User login functionality using bcrypt hashing for password encrytion
@users.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('readinglist.home',user_id=current_user.id))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('readinglist.home',user_id=user.id))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", form=form, title = "Login")

# Logout functionality
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('users.login'))

# Updating account details
@users.route("/account", methods = ['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account',form=form)
