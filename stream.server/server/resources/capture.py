import os
import glob
import json
import base64
from flask.json import jsonify
from flask_restful import Resource

from ..settings import IMAGES_DIR


class CaptureResource(Resource):

    @staticmethod
    def get():
        return jsonify(json.dumps({
            "status": 0,
            "image": base64.encodebytes(open(max(glob.glob("{directory}/*.png".format(directory=IMAGES_DIR)),
                                                 key=os.path.getctime)).read())
        }))
