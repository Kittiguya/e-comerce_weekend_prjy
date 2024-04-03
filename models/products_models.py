from app import db


class ProductModel(db.Model):
        __tablename__ = 'products'

        
        name = db.Column(db.String(50), primary_key = True)
        description = db.Column(db.String(150), nullable=False, unique=True)
        price = db.Column(db.Integer())
        

        def save_product(self):
                db.session.add(self)
                db.session.commit()

        def delete_product(self):
                db.session.delete(self)
                db.session.commit()

        def to_dict(self):
                return {
                'name': self.name,
                'description': self.description,
                'price': self.price
                }

