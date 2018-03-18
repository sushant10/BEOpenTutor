from flask import (
	Blueprint, render_template, session, g, flash, request, redirect, url_for,
	current_app, jsonify, abort, make_response
)
from run import app, mongo

db = mongo.db

class Users(db.document):
	username = db.StringField(max_length=60)
	FirstName = db.StringField(max_length=60)
	LastName = db.StringField(max_length=60)
	major = db.StringField(max_length=60)
	requested = db.BooleanField(default=False)
	requestedAs = db.ListField()
	requestedTo = db.ListField()
	InProgress = db.ListField()
	
	