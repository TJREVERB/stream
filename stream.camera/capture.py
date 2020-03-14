#!/usr/bin/env python3
import os
import sys
import json
import time
import base64
import datetime
import requests
from fakecamera import PiCamera

# from picamera import PiCamera


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.abspath(os.path.join(BASE_DIR, "captures"))
IMAGE_TYPE = "png"
RESOLUTION = (1024, 768)
HOST = "cubesat-stream.sites.tjhsst.edu"
SERVER_ENDPOINT = "https://{host}/captures".format(host=HOST)
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
        filename = f"{timestamp}.{self.image_type}"
        absolute = os.path.abspath(os.path.join(IMAGES_DIR, filename))
        self.camera.capture(absolute)
        return filename, absolute

    def process(self):
        filename, absolute = self.capture()
        with open(absolute, 'rb') as f:
            r = requests.post(
                url=self.endpoint,
                headers={"Content-Type": "application/json"},
                data=json.dumps(
                    {
                        "filename": f"{filename}", "image": base64.encodebytes(f.read()).decode("ascii")
                    }
                ))
            print(r.text)
        time.sleep(self.delay)


def main():
    camera = Camera(RESOLUTION, SERVER_ENDPOINT, IMAGES_DIR, IMAGE_TYPE, DELAY)
    camera.process()


if __name__ == "__main__":
    main()
