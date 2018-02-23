from flask import Blueprint
from .routes import init_routes

home_app = Blueprint('home', __name__)
init_routes(home_app)
