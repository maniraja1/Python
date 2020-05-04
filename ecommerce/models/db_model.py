from flask_sqlalchemy import SQLAlchemy
db_orm = SQLAlchemy()
db_mssql = SQLAlchemy().create_engine('mssql+pymssql://apptest:Sqlserver100$@localhost:1401/ecommerce',{})

#db = PyMssql(app) # Need to try this https://libraries.io/pypi/Flask-PyMssql


