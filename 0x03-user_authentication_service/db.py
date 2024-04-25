#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


DB_COLUMNS = {'id',
              'email',
              'hashed_password',
              'session_id',
              'reset_token'
              }


class DB:
    """ DB class """

    def __init__(self) -> None:
        """ Initialize a new DB instance """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """ Memoized session object """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database

        Args:
            email: The email of the user
            hashed_password: The hashed password of the user

        Returns:
            User: The newly created User object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.flush()
        self._session.commit()
        return user

    def find_user_by(self, **criteria) -> User:
        """
        Find a user by the given criteria

        Args:
            criteria: Keyword argument representing the criteria to search for

        Returns:
            User: The found User object

        Raises:
            InvalidRequestError: If no valid criteria provided
            NoResultFound: If no user is found matching the criteria
        """
        if not criteria or any(
            field not in DB_COLUMNS for field in criteria
        ):
            raise InvalidRequestError
        session = self._session
        try:
            return session.query(User).filter_by(**criteria).one()
        except NoResultFound:
            raise NoResultFound
