#!/usr/bin/env python3
"""
Basic Authentication Module for the API
"""
import base64
import binascii
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    Basic authentication class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header
        for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header value.

        Returns:
            str: The Base64 part of the Authorization header if present,
            otherwise None.
        """
        if (
            authorization_header is None or
            not isinstance(authorization_header, str)
        ):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        base64_part = authorization_header.split(' ')[1]
        return base64_part

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 string.

        Args:
            base64_authorization_header (str): The Base64 string.

        Returns:
            str: The decoded value as UTF-8 string if it's a valid Base64,
            otherwise None.
        """
        if (
            base64_authorization_header is None or
            not isinstance(base64_authorization_header, str)
        ):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user email and password from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str):
            The Base64 decoded string.

        Returns:
            Tuple[str, str]: A tuple containing user email and password,
            or (None, None) if not found or invalid.
        """
        if (
            decoded_base64_authorization_header is None or
            not isinstance(decoded_base64_authorization_header, str)
        ):
            return None

        colon_index = decoded_base64_authorization_header.find(':')

        if colon_index == -1:
            return None, None

        user_email = decoded_base64_authorization_header[:colon_index]
        user_password = decoded_base64_authorization_header[colon_index + 1:]
        return user_email, user_password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.

        Args:
            user_email (str): The email of the user.
            user_pwd (str): The password of the user.

        Returns:
            TypeVar('User'): The User instance if found and password matches,
            otherwise None.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Overload Auth and retrieve the User instance for a request"""

        authorization_header = self.authorization_header(request)

        base64_header = self.extract_base64_authorization_header(
            authorization_header)

        decoded_credentials = self.decode_base64_authorization_header(
            base64_header)

        user_email, user_password = self.extract_user_credentials(
            decoded_credentials)

        user = self.user_object_from_credentials(user_email, user_password)
        return user
