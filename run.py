from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config.from_pyfile('instance/config.py')

mongo = PyMongo(app)

from BEOpenTutor.views import *

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)