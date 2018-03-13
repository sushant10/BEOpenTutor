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

@app.route('/showall', methods=['GET'])
@auth.login_required
def main_test():
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
						'Requested To': q['requestedTo'],
						'Class Requested': q['classRequested']
					})

	return jsonify({'result' : output})



