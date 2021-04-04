import os
import json

with open('/etc/config/bookreview_config.json') as config_file:
    config = json.load(config_file)

class Config:
	#SECRET_KEY = os.environ.get('SECRET_KEY')
        SECRET_KEY = config.get('SECRET_KEY')
	#SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
        SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
