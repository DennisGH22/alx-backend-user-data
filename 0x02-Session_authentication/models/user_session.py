#!/usr/bin/env python3
"""
User Session Module for the API
"""
from models.base import Base


class UserSession(Base):
    """
    User Session class.
    """
    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize SessionAuth instance. """
        self.user_id = kwargs.get('user_id', '')
        self.session_id = kwargs.get('session_id', '')

        super().__init__(*args, **kwargs)
