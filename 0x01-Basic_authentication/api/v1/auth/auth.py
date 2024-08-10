#!/usr/bin/env python3
""" Auth class
"""

from flask import request


class Auth:
    """ Auth Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ TODO require_auth implement
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ TODO authorization_header implementation
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ TODO current_user implementation
        """
        return None
