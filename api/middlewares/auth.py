# middlewares/auth.py
class AuthMiddleware(object):

    def process_request(self, req, resp):
        token = req.get_header('Authorization')
        req.context['token'] = token