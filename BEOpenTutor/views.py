from flask import (
    Blueprint, render_template, session, g, flash, request, redirect, url_for,
    current_app, jsonify
)

from run import app

@app.route('/', methods=['GET'])
def get_tasks():
    return 200
    