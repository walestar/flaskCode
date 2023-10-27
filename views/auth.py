from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from.index import index_views

from App.controllers import (
    create_user,
    jwt_authenticate,
    login 
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''

@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@auth_views.route('/courses', methods=['GET'])
@login_required
def get_courses():
    return jsonify({“name”: “course name”,“description: :”course description”,“credits”:”course credits”}
)


@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    user = login(data['userID'], data['password'])
    if user:
        login_user(user)
        return 'user logged in!'
    return 'Invalid ID or password given', 401

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    data = request.form
    user = login(data['userID'], data['password'])
    return 'logged out!'

'''
API Routes
'''

@auth_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@auth_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['userID'], data['password'])
    return jsonify({'message': f"user {data['userID']} created"})

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
  data = request.json
  token = jwt_authenticate(data['userID'], data['password'])
  if not token:
    return jsonify(message='Invalid ID or password given'), 401
  return jsonify(access_token=token)

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"userID: {jwt_current_user.username}"})
