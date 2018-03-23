from flask import Flask
from flask_pymongo import PyMongo
import logging

app = Flask(__name__)

app.config.from_pyfile('instance/config.py')

mongo = PyMongo(app)

from BEOpenTutor.views import *

if __name__ == '__main__':
	logger = logging.getLogger('werkzeug')
	handler = logging.FileHandler('access.log')
	logger.addHandler(handler)
	app.run(host='0.0.0.0', port=80)