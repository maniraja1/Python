
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class Product(db.Model):

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"product('{self.product_name}')"

    def insertproduct(self):
        db.session.add(self.productname)

    @staticmethod
    def getProduct(id=None, name=None):
        print(f"ID: {id}, name: {name}")
        if id is not None:
            return f"This is the product home page ID: {id}"
        elif name is not None:
            return f"This is the product home page Name: {name}"
        else:
            return "This is the product home page"
