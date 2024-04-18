#!/usr/bin/env python3
""" Module of Session Authentication views
"""
from os import getenv
from flask import jsonify, request
from api.v1.views import app_views
from api.v1.app import auth
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session():
    """ POST /api/v1/auth_session/login
    Return:
      - the dictionary representation of the User, otherwise status code
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    user_json = user.to_json()

    response = jsonify(user_json)
    response.set_cookie(
        getenv("SESSION_NAME"), value=session_id
    )

    return response
