from flask_smorest import Blueprint

bp = Blueprint("products", __name__, description="Routes for products")

from . import routes