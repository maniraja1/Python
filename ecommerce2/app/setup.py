from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import os
from logging import Formatter, INFO
from logging.handlers import RotatingFileHandler


def setupSQLConnectionORM(app):
    db = SQLAlchemy()
    registerDatabase(app, db)
    initdatabase(app,db)
    return db # ORM object

def setUpSQLConnection(app):
    return SQLAlchemy().create_engine(app.config['SQLALCHEMY_DATABASE_URI'], {})

def registerDatabase(app, db):
    db.init_app(app)

def loadconfig(app):
    app.config.from_pyfile('config.py')

def initdatabase(app, db):
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


def create_app(app):
    loadconfig(app)
    initlogging(app)
    return app


flask_app = Flask(__name__)
flask_app = create_app(flask_app)
db = setupSQLConnectionORM(flask_app)
db_mssql = setUpSQLConnection(flask_app)

