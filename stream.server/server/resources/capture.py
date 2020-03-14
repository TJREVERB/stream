import os
import glob
from flask.json import jsonify
from flask_restful import Resource

from ..settings import IMAGES_DIR


class CaptureResource(Resource):

    @staticmethod
    def get():
        file = max(glob.glob("{directory}/*".format(directory=IMAGES_DIR)), key=os.path.getctime)
        return jsonify(
            {
                "status": 0,
                "image": file[file.find('static'):]
            }
        )
