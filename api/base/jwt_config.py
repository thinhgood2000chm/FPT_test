from datetime import datetime, timedelta
import os
from urllib.error import HTTPError

from dotenv import load_dotenv
import jwt
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from api.v1.constant import AUTHEN_TYPE

load_dotenv()


def generate_jwt_token(username):
    """
    Generates a JSON Web Token that stores this user's ID and has an expiry
    date set to 60 days into the future.
    """
    datetime.utcnow() + timedelta(minutes=30)

    token = jwt.encode({
        'username': username,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, os.getenv('JWT_SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return token


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != AUTHEN_TYPE.encode():
            raise exceptions.AuthenticationFailed({
                'description': 'bearer token not found'
            })
        try:
            payload = jwt.decode(auth[1], os.getenv('JWT_SECRET_KEY'), algorithms=[os.getenv("ALGORITHM")])
            username = payload.get("username")

            if username is None:
                raise exceptions.AuthenticationFailed({
                    'description': 'bearer token not valid'
                })

            setattr(request, "username", username)

        except jwt.exceptions.InvalidTokenError as e:
            raise exceptions.AuthenticationFailed({
                'description': 'Invalid JWT'
            })
        return None

