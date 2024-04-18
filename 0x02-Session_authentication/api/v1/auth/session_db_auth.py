#!/usr/bin/env python3
"""
Database Session Authentication Module for the API
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    Database Session Authentication Class.
    """
    def create_session(self, user_id=None):
        """ Create a Session ID. """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dict = {
            "user_id": user_id,
            "session_id": session_id
        }

        user_session = UserSession(**session_dict)
        user_session.save()

        return session_id
    
    def user_id_for_session_id(self, session_id=None):
        """ Get User ID from the session dictionary. """
        if session_id is None:
            return None

        user_session = UserSession.search({"session_id": session_id})
        if user_session is None:
            return None

        return user_session.user_id
    
    def destroy_session(self, request=None):
        """ Destroy the UserSession. """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            user_session.delete()
            return True

        return False
