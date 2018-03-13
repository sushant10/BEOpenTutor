from flask import (
	Blueprint, render_template, session, g, flash, request, redirect, url_for,
	current_app, jsonify
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
	u = mongo.db.Majors
	output = []

	for q in u.find():
		output.append({
						'Major' : q['Major'],  
						'Classes': q['Classes'], 
					})

	return jsonify(output)

@app.route('/find/<string:major>&<int:classreq>', methods=['GET'])
def find_tutor(major,classreq):
	u = mongo.db.Users
	output=[]

	for q in u.find({"major":major}):
		output.append({
						'Username' : q['username'],  
						'First Name': q['FirstName'], 
						'Last Name': q['LastName'], 
						'Major' : q['major']
						})

	return jsonify(output) 

@app.route('/find/requestTutor', methods=['POST'])
def requestTutor():
	return None


