from flask import Flask
from flask_cors import CORS
from flask.blueprints import Blueprint
from flask.json import jsonify

from . import routes
from . import settings


app = Flask(__name__)
app.debug = settings.DEBUG


for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=settings.APPLICATION_ROOT)

app.route()
