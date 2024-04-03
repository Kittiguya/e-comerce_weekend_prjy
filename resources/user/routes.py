from flask import Flask, abort, jsonify, request
from flask.views import MethodView
from schemas import UserSchema, UserWithPostsSchemas
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies



from . import bp
from app import app
from models.user_models import UserModel





@app.route('/users')
class UserList(MethodView):
    @bp.response(200, UserSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return jsonify(UserSchema().dump(users)), 200

    @jwt_required
    @bp.arguments(UserSchema)
    @bp.response(201, UserWithPostsSchemas)
    def post(self, data):
        try:
            user = UserModel()
            user.from_dict(data)
            user.save_user()
            response_data = UserWithPostsSchemas().dump(user)
            return jsonify(response_data), 201
        except Exception as e:
            abort(400, message="User already exists, please try a different one")

@bp.route('/user/<int:id>')
class User(MethodView):
    @bp.response(200, UserWithPostsSchemas)
    def get(self, id):
        user = UserModel.query.get(id)
        if user:
            return jsonify(UserWithPostsSchemas().dump(user)), 200
        else:
            abort(404, message="User not found")

    @jwt_required
    @bp.arguments(UserSchema)
    @bp.response(200, UserWithPostsSchemas)
    def put(self, data, id):
        user = UserModel.query.get(id)
        if user:
            user.from_dict(data)
            user.save_user()
            return jsonify(UserWithPostsSchemas().dump(user)), 200
        else:
            abort(404, message="User not found")

    @jwt_required
    @bp.response(200, {"message": "User has been deleted"})
    def delete(self, id):
        user = UserModel.query.get(id)
        if user:
            user.delete_user()
            return jsonify(message="User has been deleted"), 200
        else:
            abort(404, message="User not found")