#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt hashpw with a salt

    Args:
        password: The password to be hashed

    Returns:
        bytes: The salted hash of the input password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


class Auth:
    """ Auth class to interact with the authentication database. """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Args:
            email: The email of the user.
            password: The password of the user.

        Returns:
            User: The newly registered user object.

        Raises:
            ValueError: If a user with the email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(
                email=email, hashed_password=hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Check if the provided email and password are valid for login.

        Args:
            email: The email of the user.
            password: The password to check.

        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        hashed_password = user.hashed_password
        input_password = password.encode()
        return bcrypt.checkpw(input_password, hashed_password)

def _generate_uuid() -> str:
    """
    Generate a string representation of a new UUID.
    
    Returns:
        str: The string representation of the generated UUID.
    """
    return str(uuid.uuid4())
