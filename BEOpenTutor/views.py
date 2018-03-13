from flask import (
	Blueprint, render_template, session, g, flash, request, redirect, url_for,
	current_app, jsonify
)

from run import app, mongo

@app.route('/', methods=['GET'])
def main_test():
	u = mongo.db.Users
	output = []

	for q in u.find():
		output.append({'email' : q['username'], 'major' : q['major']})

	return jsonify({'result' : output})

