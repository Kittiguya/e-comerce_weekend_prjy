from app import db



class CartModel(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)


    def save_cart(self):
        db.session.add(self)    
        db.session.commit()    
        
    def delete_cart(self):
        db.session.delete(self)
        db.session.commit()