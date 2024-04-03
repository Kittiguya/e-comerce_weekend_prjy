from flask_smorest import Blueprint

bp = Blueprint("user", __name__, description="Routes for users")
from . import routes