SQLALCHEMY_DATABASE_URI= "mssql+pymssql://apptest:Sqlserver100$@localhost:1401/ecommerce"
SQLALCHEMY_TRACK_MODIFICATIONS = "False"
SQLALCHEMY_TRACK_MODIFICATIONS = "False"
LOGDIR= "logging"
SECRET_KEY = 'very_very_secure_and_secret'
CELERY_BROKER_URL = 'redis://localhost:6379/0'
RESULT_BACKEND = 'redis://localhost:6379/0'