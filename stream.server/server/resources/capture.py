import os
import glob
import base64
from flask.json import jsonify
from flask_restful import Resource

from ..utils import validate, BodyArg
from ..settings import IMAGES_DIR


class CaptureResource(Resource):

    @staticmethod
    def get():
        files = sorted(glob.glob("{directory}/*".format(directory=IMAGES_DIR)), key=os.path.getctime)
        return jsonify(
            {
                "status": 0,
                "image": [file[file.find('static'):] for file in files]
            }
        )

    @staticmethod
    @validate(
        BodyArg("filename", help="Filename of image"),
        BodyArg("image", help="base64 encoded image"),
    )
    def post(**kwargs):
        with open(os.path.abspath(os.path.join(IMAGES_DIR, kwargs['filename'])), 'wb') as w:
            w.write(base64.decodebytes(kwargs['image'].encode("ascii")))
        return jsonify({"status": 0})
