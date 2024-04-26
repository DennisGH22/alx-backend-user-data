#!/usr/bin/env python3
"""
Flask App
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def index():
    """ Route to return a welcome message. """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """ Endpoint to register a new user. """
    try:
        email = request.form["email"]
        password = request.form["password"]
        new_user = AUTH.register_user(email, password)
        return jsonify({
            "email": new_user.email,
            "message": "user created"
        }), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """ Endpoint to log in a user. """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        abort(401)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    if session_id:
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    """ Endpoint to log out a user. """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        return jsonify({"message": "User not found"}), 403


@app.route("/profile", methods=["GET"])
def profile():
    """ Endpoint to retrieve user profile. """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """ Endpoint to generate a reset password token. """
    email = request.form.get("email")
    if not email:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 403


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """ Endpoint to update the password. """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
