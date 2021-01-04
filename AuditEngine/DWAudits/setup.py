import sqlalchemy
import config

def setUpSQLConnection():
    return sqlalchemy.create_engine(config.SQLALCHEMY_DATABASE_URI)


db_mssql = setUpSQLConnection()
