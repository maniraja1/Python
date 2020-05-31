from createapp import flask_app
from celery import Celery
from time import sleep
from flask_sqlalchemy import SQLAlchemy
import json
from app.models.product_model import Product


celery_client = Celery(flask_app.name, broker='redis://localhost:6379/0')
celery_client.conf.update(flask_app.config)


with open('app.config.json') as f:
    config = json.load(f)

db_mssql = SQLAlchemy() # adhoc sql object
db_mssql = SQLAlchemy().create_engine(config['SQLALCHEMY_DATABASE_URI'],{})



@celery_client.task
def InsertAsync(name):
    print("Starting")
    sleep(15)
    with flask_app.app_context():
        with db_mssql.connect() as connection:
            cursor = connection.execute(f"Insert into product (product_name) values ('{name}')")
            print(f"Success")

@celery_client.task
def InsertAsync2(name):
    print("Starting")
    sleep(15)
    with flask_app.app_context():
        with open('app.config.json') as f:
            config2 = json.load(f)
            flask_app.config.update(config2)

        db = SQLAlchemy()
        db.init_app(flask_app)
        db.create_all()
        Product(product_name=name).insertproduct()
        print(f"Success")




