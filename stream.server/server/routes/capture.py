from flask import Blueprint
from flask_restful import Api

from ..resources import CaptureResource

CAPTURE_BLUEPRINT = Blueprint("captures", __name__)
Api(CAPTURE_BLUEPRINT).add_resource(
    CaptureResource, "/captures"
)