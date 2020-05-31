SECRET_KEY = 'very_very_secure_and_secret'
CELERY_BROKER_URL = 'redis://localhost:6379/0'
RESULT_BACKEND = 'redis://localhost:6379/0'
include=("app.models.product_model.InsertAsync",)
SQLALCHEMY_TRACK_MODIFICATIONS = "False"
