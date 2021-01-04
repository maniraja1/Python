from app import flask_app, db_mssql
from time import sleep
from app.models.product_model import Product
from celery import Celery

celery_client = Celery(flask_app.name, broker=flask_app.config['CELERY_BROKER_URL'])
celery_client.conf.update(flask_app.config)

@celery_client.task
def InsertAsync(name):
    print("Starting")
    sleep(15)
    with flask_app.app_context():
        with db_mssql.connect() as connection:
            connection.execute(f"Insert into product (product_name) values ('{name}')")
            print(f"Success")

@celery_client.task
def InsertAsync2(name):
    print("Starting")
    sleep(15)
    with flask_app.app_context():
        Product(product_name=name).insertproduct()
        print(f"Success")




