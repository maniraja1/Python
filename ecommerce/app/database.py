from flask_sqlalchemy import SQLAlchemy
import json

with open('app.config.json') as f:
    config = json.load(f)

db_orm = SQLAlchemy() # ORM object
db_mssql = SQLAlchemy() # adhoc sql object
db_mssql = SQLAlchemy().create_engine(config['SQLALCHEMY_DATABASE_URI'],{})

#db = PyMssql(app) # Need to try this https://libraries.io/pypi/Flask-PyMssql