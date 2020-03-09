from flask import Flask
from flask import Blueprint
from flask_restplus import Api
from models import db
import routes as product ## Do not move this to the top its here because of circular reference

product_bp = Blueprint('product', __name__, url_prefix='/swagger')
product_api = Api(product_bp, title='Ecommerce', description='Manis Ecommerce API')
product_api.add_namespace(product.product_ns)

flask_app = Flask(__name__)
flask_app.register_blueprint(product_bp)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(flask_app)

with flask_app.app_context():
    db.create_all()

flask_app.run(debug=True)





