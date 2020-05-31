from app import create_app
from createapp import flask_app

flask_app = create_app(flask_app)
flask_app.run(debug=True)

