from app import flask_app
from app.registerblueprint import registerBluePrint

registerBluePrint(flask_app)
flask_app.run(debug=True)
