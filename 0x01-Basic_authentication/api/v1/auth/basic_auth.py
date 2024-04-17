#!/usr/bin/env python3
"""
Basic Authentication Module for the API
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic authentication class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header value.

        Returns:
            str: The Base64 part of the Authorization header if present, otherwise None.
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        base64_part = authorization_header.split(' ')[1]
        return base64_part
