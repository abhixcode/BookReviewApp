from flask import render_template, url_for, flash, redirect, request, Blueprint
#from flaskblog.main.forms import RegistrationForm, LoginForm, UpdateAccountForm, ListForm
from bookreview.models import User, Readinglist
from bookreview import create_app,db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def booklist():
	readinglist = "abc"
#    readinglist = Readinglist.query.all()
	return render_template("booklist.html", readinglist=readinglist)