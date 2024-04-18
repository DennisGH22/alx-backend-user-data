#!/usr/bin/env python3
""" Module of Session Authentication views
"""
from os import getenv
from flask import jsonify, abort, request
from api.v1.views import app_views
from api.v1.app import auth
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session():
    """ POST /api/v1/auth_session/login
    Return:
      - the dictionary representation of the User, otherwise status code
    """
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    if not user_email:
        return jsonify({"error": "email missing"}), 400

    if not user_password:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': user_email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(user_password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    user_json = user.to_json()

    response = jsonify(user_json)
    response.set_cookie(getenv("SESSION_NAME"), session_id)

    return response


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False
)
def logout():
    """ DELETE /api/v1/auth_session/logout
    Return:
      - An empty JSON dictionary with the status code 200, otherwise False
    """
    session_id = auth.destroy_session(request)
    if not session_id:
        abort(404)

    return jsonify({}), 200
