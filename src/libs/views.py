"""
Common Libraries to be used in system level
"""
from flask.views import MethodView
from flask_login import login_required

class AuthorizedView(MethodView):
    """
    Base class for authorized view.
    """
    decorators = [login_required]

    def __init__(self):
        pass

