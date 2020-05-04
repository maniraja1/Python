'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
'''
from models.db_model import db_orm as db, db_mssql
from flask import jsonify
from sqlalchemy import engine

class Product(db.Model):

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self,product_id = None, product_name=None):
        self.product_name=product_name
        self.product_id=product_id

    def __repr__(self):
        return f"product({self.product_id}, '{self.product_name}')"

    def serialize(self):
        return {"id": self.product_id,
                "name": self.product_name}

    def insertproduct(self):
        if self.product_name is None:
            raise ValueError("Product Name cannot be None")
        '''
        if self.product_id is None:
            raise ValueError("Product ID cannot be None")
        '''

        if self.getProductByID() is not None:
            raise ValueError (f"Product with ID:{self.product_id} already exists")

        if self.getProductByName() is not None:
            raise ValueError (f"Product with Name: {self.product_name} already exists")

        db.session.add(self)
        db.session.commit()

        return "Success"

    @staticmethod
    def getAllProducts():
        ret_json = []
        for x in Product.query.all():
            ret_json.append (x.serialize())
        return ret_json


    def getProductByID(self):
        x = Product.query.get(self.product_id)
        if x:
            return x.serialize()
        else:
            return None

    def getProductByName(self):
        x = Product.query.filter_by(product_name=self.product_name).all()
        ## Not sure if this is the right way to do this. This returns a list of products
        ## Should this collection be a class by itself
        if x:
            return [y.serialize() for y in x]
        else:
            return None

    ## Running adhoc SQL
    def getTopNProducts(n):
        with db_mssql.connect() as connection:
            cursor = connection.execute(f'SELECT top {n} * FROM product')
            return jsonify({'result': [dict(row) for row in cursor]})





