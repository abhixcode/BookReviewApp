# We initialise the app here with config, database, login manager and bcrypt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from bookreview.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)

	# We import the blue prints and register them with the app
	from bookreview.users.routes import users
	from bookreview.readinglist.routes import readinglist
	from bookreview.main.routes import main
	from bookreview.errors.handlers import errors
	app.register_blueprint(users)
	app.register_blueprint(readinglist)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app