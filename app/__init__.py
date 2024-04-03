from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager

from Config import Config



app = Flask(__name__)
app.config.from_object(Config)
app.config["JWT_SECRET_KEY"] = "SECRET_KEY"
api = Api(app)
jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from resources.user import bp as users_bp
app.register_blueprint(users_bp)

from resources.cart import bp as cart_bp
app.register_blueprint(cart_bp)

from resources.products import bp as product_bp
app.register_blueprint(product_bp)