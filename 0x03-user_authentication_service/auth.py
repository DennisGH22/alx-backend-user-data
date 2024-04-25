#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt


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
