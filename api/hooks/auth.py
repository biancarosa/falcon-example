# hooks/auth.py
import falcon
from api.models.user_token import UserToken

def authorize():
    def hook(req, resp, resource, params):
        token = req.context.get('token')
        if token is None:
            description = ('Please provide an auth token as part of the request.')
            raise falcon.HTTPUnauthorized('Auth token required', 'Auth token required', description, href='http://docs.example.com/auth')
            user_token = UserToken.get_by_token(token)
            if not user_token or not user_token.is_valid():
                description = ('The provided auth token is not valid. Please request a new token and try again.')
                raise falcon.HTTPUnauthorized('Authentication required', 'Authentication required', description, href='http://docs.example.com/auth', scheme='Token; UUID')
            else:
                req.context['current_user'] = user_token.user

    return hook