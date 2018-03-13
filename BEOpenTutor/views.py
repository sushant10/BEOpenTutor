from flask import (
	Blueprint, render_template, session, g, flash, request, redirect, url_for,
	current_app, jsonify, abort, make_response
)
from flask_httpauth import HTTPBasicAuth
from run import app, mongo
from instance.config import ADMIN_PSW

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'admin':
        return ADMIN_PSW
    return None

@app.route('/allusers', methods=['GET'])
@auth.login_required
def all_users():
	u = mongo.db.Users
	output = []

	for q in u.find():
		output.append({
						'Username' : q['username'],  
						'First Name': q['FirstName'], 
						'Last Name': q['LastName'], 
						'Major' : q['major'], 
						'Requested': q['requested'], 
						'Requested As': q['requestedAs'],
						'Requested To': q['requestedTo']
					})

	return jsonify(output)

@app.route('/find/allmajor', methods=['GET'])
def all_majors():
	m = mongo.db.Majors
	output = []

	for q in m.find():
		output.append({
						'Major' : q['Major'],  
						'Classes': q['Classes'], 
					})

	return jsonify(output)

@app.route('/find/<string:major>&<string:classreq>', methods=['GET'])
def find_tutor(major,classreq):
	u = mongo.db.Users
	output=[]
	m = mongo.db.Majors

	if len(major) == 0:
		abort(400)
	if not (m.find({"Classes":{"$all": [classreq]}}).count() >0):
		abort(400)
	if not (m.find({"Major":major}).count() >0):
		abort(400)

	for q in u.find({"major":major}):
		output.append({
						'Username' : q['username'],  
						'First Name': q['FirstName'], 
						'Last Name': q['LastName'], 
						'Major' : q['major']
						})

	return jsonify(output), 200

@app.route('/find/requestTutor', methods=['POST'])
def requestTutor():

	return "Requested"

@app.errorhandler(400)
def bad_search(error):
    return make_response(jsonify({'error': 'Invalid input'}), 400)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Input not found'}), 404)