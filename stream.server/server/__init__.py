from flask import Flask, send_from_directory
from flask_cors import CORS
from flask.blueprints import Blueprint
from flask.json import jsonify

from . import routes
from . import settings

app = Flask(__name__, static_url_path=settings.STATIC_ROOT)
CORS(app)
app.debug = settings.DEBUG


for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=settings.APPLICATION_ROOT)


@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(host=settings.HOST, port=settings.PORT)
