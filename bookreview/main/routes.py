from flask import render_template, url_for, flash, redirect, request, Blueprint
from bookreview.models import User, Readinglist
from bookreview import create_app,db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

#@main.route('/')
@login_required
def booklist():
	readinglist = "abc"
	return render_template("booklist.html", readinglist=readinglist)
