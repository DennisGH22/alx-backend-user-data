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
            bool: Always returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Placeholder method to get authorization header.

        Args:
            request: The Flask request object.

        Returns:
            str: Always returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method to get the current user.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar('User'): Always returns None.
        """
        return None
