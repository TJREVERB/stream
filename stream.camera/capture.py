#!/usr/bin/env python3
import os
import sys
import time
import base64
import datetime
import requests
from fakecamera import PiCamera
#from picamera import PiCamera


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.abspath(os.path.join(BASE_DIR, "captures"))
IMAGE_TYPE = "png"
RESOLUTION = (1024, 768)
HOST = "198.38.16.84"
PORT = 5000
SERVER_ENDPOINT = "http://{host}:{port}/captures".format(host=HOST, port=PORT)
DELAY = 5


class Camera:
    def __init__(
            self,
            resolution: tuple,
            endpoint: str,
            images_dir: str,
            image_type: str,
            delay: int,
    ):
        self.camera = PiCamera()
        self.endpoint = endpoint
        self.images_dir = images_dir
        self.image_type = image_type
        self.delay = delay

        if not os.path.exists(self.images_dir):
            os.mkdir(self.images_dir)

        self.camera.resolution(resolution)
        self.camera.start_preview()
        time.sleep(2)

    def capture(self):
        timestamp = datetime.datetime.fromtimestamp(
            time.time()
        ).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        filename = os.path.abspath(os.path.join(IMAGES_DIR, f"{self.images_dir}/{timestamp}.{self.image_type}"))
        self.camera.capture(filename)
        return filename

    def process(self):
        with open(self.capture(), 'rb') as f:
            requests.post(self.endpoint, data={"filename": filename, "image": base64.encodebytes(f.read())})
        time.sleep(self.delay)


def main():
    camera = Camera(RESOLUTION, SERVER_ENDPOINT, IMAGES_DIR, IMAGE_TYPE, DELAY)
    camera.process()


if __name__ == "__main__":
    main()
