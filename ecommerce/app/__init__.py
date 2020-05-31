from flask import Blueprint
from flask_restplus import Api
from app.database import db_orm as db
from app.database import db_mssql
import app.routes as product ## Do not move this to the top its here because of circular reference
import json
import os
from logging import Formatter, INFO
from logging.handlers import RotatingFileHandler


def registerBluePrint(app):
    product_bp = Blueprint('product', __name__, url_prefix='/swagger')
    product_api = Api(product_bp, title='Ecommerce', description='Manis Ecommerce API')
    product_api.add_namespace(product.product_ns)
    app.register_blueprint(product_bp)

def registerDatabase(app):
    db.init_app(app)

def loadconfig(app):
    print(os. getcwd())
    with open('app.config.json') as f:
        config = json.load(f)
    app.config.update(config)


def initdatabase(app):
    with app.app_context():
        db.create_all()

def initlogging(app):
    with open('app.config.json') as f:
        config = json.load(f)

    if not os.path.exists(config['LOGDIR']):
        os.mkdir(config['LOGDIR'])

    file_handler = RotatingFileHandler(f"{config['LOGDIR']}/ecommerce.log", maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(INFO)
    app.logger.info('ecommerce startup')



def create_app(flask_app):
    loadconfig(flask_app)
    registerBluePrint(flask_app)
    registerDatabase(flask_app)
    initdatabase(flask_app)
    initlogging(flask_app)
    return flask_app




