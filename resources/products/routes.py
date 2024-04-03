from flask import abort, jsonify, request
from flask.views import MethodView

from . import bp
from app import app
from schemas import ProductsSchemas, ProductsWithPostsSchemas
from models.products_models import ProductModel
from app import db



@bp.route('/products')
class ProductsList(MethodView):

    def get(self):
        products = ProductModel.query.all()
        return [product.to_dict() for product in products], 200

    @bp.response(201, ProductsWithPostsSchemas)
    def post(self):
        try:
            data = request.get_json()  
            if not data:
                return jsonify({'message': 'No JSON data received'}), 400

           
            errors = ProductsSchemas().validate(data)
            if errors:
                return jsonify({'message': 'Validation errors', 'errors': errors}), 400

            
            product = ProductModel(**data) 
            db.session.add(product)
            db.session.commit()

            return jsonify({'message': 'Product created successfully', 'product': product.to_dict()}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 400


    @bp.route('/Products/<string:name>')
    @bp.response(200, ProductsWithPostsSchemas)
    @bp.arguments(ProductsSchemas, location='json')
    def put(self, name, data):
        product = ProductModel.query.get(name)
        if product:
            product.from_dict(data)
            product.save_product()
            return {"message" : "product updated"}, 200
        else:
            abort(400, message="not a valid product")
    
    def delete_product(self, name):
        product = ProductModel.query.get(name)
        if product:
            product.del_product()

            return {"message" : "Product has been deleted"}, 200
        else:
            abort(400, message="not a valid product")
                
            