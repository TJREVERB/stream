import os
import glob
from flask.json import jsonify
from flask_restful import Resource

from ..settings import IMAGES_DIR


class CaptureResource(Resource):

    @staticmethod
    def get():
        files = glob.glob("{directory}/*.png".format(directory=IMAGES_DIR))
        latest = max(files, key=os.path.getctime)
        return jsonify({
            "image": open(latest, "rb").read()
        })
