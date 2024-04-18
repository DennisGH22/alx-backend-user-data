#!/usr/bin/env python3
"""
Session Authentication Expiry Module for the API
"""
from os import getenv
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    Session expiry date class.
    """
    def __init__(self):
        """ Initialize SessionAuth instance. """
        session_duration_value = getenv("SESSION_DURATION")
        try:
            self.session_duration = int(session_duration_value)\
                if session_duration_value else 0
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Create a Session ID. """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dict = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dict

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Get User ID from the session dictionary. """
        if session_id is None:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None

        if self.session_duration <= 0:
            return session_dict.get("user_id")

        created_at = session_dict.get("created_at")
        if created_at is None:
            return None

        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if datetime.now() > expiration_time:
            return None

        return session_dict.get("user_id")
