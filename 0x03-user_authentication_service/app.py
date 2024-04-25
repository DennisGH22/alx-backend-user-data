#!/usr/bin/env python3
"""
Flask App
"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
