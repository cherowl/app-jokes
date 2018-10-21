from flask import Response, current_app
from src.auth_handlers import auth

@auth.errorhandler(401)
def login_failed(e):
    # resp = jsonify(e.to_dict())
    return Response(
            'Could not verify your access level for that URL.\n'
            'You have to login with proper credentials', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'})
