from flask import abort
from flask.views import MethodView
from schemas import CartSchemas, CartWithPostsSchemas
from . import bp
from app import app

from models.cart_models import CartModel




@bp.route('/cart')
class CartList(MethodView):

    @bp.response(200, CartSchemas(many=True))
    def get(self):
        return CartModel.query.all()


    @bp.arguments(CartWithPostsSchemas)
    @bp.response(201, CartSchemas)
    def post(self, data):
        try:
            cart = CartModel()
            
            cart.save_cart()
            return cart
        except:
            abort(400, message="genre already exists")
        

    @bp.arguments(CartSchemas)
    @bp.response(201, CartWithPostsSchemas)
    def update_cart(self, data, id):
        cart = CartModel.query.get(id)
        if cart:
            cart.from_dict(data)
            cart.save_cart()
            return {'message' : "genre updated"}, 201
        else:
            abort(300, message="not a valid genre")


    def delete_cart(self, id):
        cart = CartModel.query.get(id)
        if cart:
            cart.del_cart()
            return {"message" : "user has been deleted"}, 200
        abort(400, message="not a valid genre")
