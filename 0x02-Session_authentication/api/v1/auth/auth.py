#!/usr/bin/env python3
"""
Authentication Module for the API
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Manages the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Placeholder method to require authentication.

        Args:
            path: The path being accessed.
            excluded_paths: List of paths to exclude from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        path = path.rstrip('/') + '/'

        for excluded_path in excluded_paths:
            if '*' in excluded_path:
                wildcard_index = excluded_path.index('*')
                if path.startswith(excluded_path[:wildcard_index]):
                    return False
            elif path.startswith(excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Placeholder method to get authorization header.

        Args:
            request: The Flask request object.

        Returns:
            str: The value of the Authorization header if present,
            otherwise None.
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method to get the current user.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar('User'): Always returns None.
        """
        return None

    def session_cookie(self, request=None):
        """
        Placeholder method to get the session cookie value.

        Args:
            request: The Flask request object.

        Returns:
            The session cookie value.
        """
        if request is None:
            return None

        SESSION_NAME = getenv('SESSION_NAME')
        cookie_value = request.cookies.get(SESSION_NAME)

        return cookie_value
