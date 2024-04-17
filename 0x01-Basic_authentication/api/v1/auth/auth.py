#!/usr/bin/env python3
"""
Authentication Class for the API
"""
from flask import request
from typing import List, TypeVar


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
            if path.startswith(excluded_path):
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
