from flask import Flask
from flask import Blueprint
from flask_restplus import Api
from product import product

product_bp = Blueprint('product', __name__, url_prefix='/swagger')
product_api = Api(product_bp, title='Ecommerce', description='Manis Ecommerce API')
product_api.add_namespace(product.product_ns)


flask_app = Flask(__name__)
flask_app.register_blueprint(product_bp)
flask_app.run(debug=True)