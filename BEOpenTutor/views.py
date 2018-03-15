# need to handle more errors!!

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


'''
	base '/' to check server status
'''
@app.route('/', methods=['GET','POST','PUT'])
@auth.login_required
def og():
	return "Server running!"

'''
	admin request to get all current users and sensitive data
'''
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


'''
	data sending
		all majors and classes
'''
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

# add more input error handling 
'''
	data recieving
		major: search major
		classreq: search class
	data sending
		list of all possible tutors
			username
			first name
			last name
			major
'''
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


# add more error handling and input issues later
# make seperate func for error handling
'''
	data recieving via post:
		username: user requesting
		class: class requested
		major: major requested
		requestedTutor: tutor requested
	data sending back:
		requested //None
'''
@app.route('/find/requestTutor', methods=['POST'])
def requestTutor():
	if not request.values :
		abort(400)
	u=mongo.db.Users
	output=[]

	# error handling move to another func 
	if 'requestedTutor' not in request.values:
		abort(400)
	if 'class' not in request.values:
		abort(400)
	if 'major' not in request.values:
		abort(400)
	if type(request.values['username']) !=str:
		abort(400)
	if not (u.find({"username":request.values['username']}).count() >0):
		abort(404)
	if not (u.find({"username":request.values['requestedTutor']}).count() >0):
		abort(404)


	toadd ={
				"username": request.values['requestedTutor'],
				"class":{
				request.values['major']:request.values['class']
				},
				"accepted":False,
				"denied":False
	}
	u.update({'username': request.values['username']},{"$push":{"requestedTo":toadd}})

	u.update({"username":request.values['requestedTutor']},{"$set":{"requested":True}})
	u.update({'username': request.values['requestedTutor']},{"$push":{"requestedAs":request.values['username']}})


	return "Requested", 201

'''
	data recieving 
		username: current user logged in
	data sending
		list of all requests
			username
			first name 
			last name
'''

@app.route('/requested', methods=['GET'])
def requested_user():
	if not request.values :
		abort(400)

	u=mongo.db.Users
	output=[]
	user=u.find({"username":request.values['username']})

	if type(request.values['username']) !=str:
		abort(400)
	if not (user.count() >0):
		abort(404)

	for q in user:
		for r in q['requestedAs']:
			tr= u.find({"username":r})
			for h in tr:
				flag=True
				req_to = h['requestedTo']
				class_req=[]
				for e in req_to:
					if e['username']==request.values['username']:
						class_req.append(e['class'])
					if e['denied']==True:
						flag=False
				
				if(flag):
					output.append({
							'Username' : h['username'],  
							'First Name': h['FirstName'], 
							'Last Name': h['LastName'], 
							'Major' : h['major'],
							'Class requested': class_req
							})

	return jsonify(output)


'''
	data recieved
		username : logged in user
		requestedStudent : student accepting/ rejected
		class (accepted/rejected) : Major + Class in same format
		accept/denied : True/False
	data sent back
		accepted/denied
'''
@app.route('/requested/confirm', methods=['POST'])
def req_confirm():
	if not request.values :
		abort(400)

	u=mongo.db.Users
	output=[]

	user=u.find({"username":request.values['username']})
	reqStudent= u.find({"username":request.values['requestedStudent']})
	
	# check for all data recieved
	if type(request.values['username']) !=str:
		abort(400)
	if type(request.values['requestedStudent'] !=str):
		abort(400)
	if not (user.count() >0):
		abort(404)
	if not (reqStudent.count() >0):
		abort(404)
	







# ~~~~~~~~~ all error handling methods ~~~~~~~~~~

@app.errorhandler(400)
def bad_search(error):
	return make_response(jsonify({'error': 'Invalid input'}), 400)


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Input not found'}), 404)



