#!/usr/bin/env python3
import os
import cv2
import sys
import time
import socket
import datetime
from picamera import PiCamera

IMAGES_DIR = "captures"
IMAGE_TYPE = "png"
RESOLUTION = (1024, 768)
TARGET = ("198.38.16.84", 5000)  # (host, port)
DELAY = 5
VID_FILENAME = "../../stream_vid.mp4"

class Camera:
    def __init__(
        self,
        resolution: tuple,
        s: socket.socket,
        images_dir: str,
        image_type: str,
        delay: int,
    ):
        self.camera = PiCamera()
        self.socket = s
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
        filename = f"{self.images_dir}/{timestamp}.{self.image_type}"
        self.camera.capture(filename)
        return filename


    def process(self):
        filename = self.capture()
        self.socket.send(cv2.imencode("." + self.image_type, cv2.imread(filename))[1].tobytes())
        time.sleep(self.delay)


class PseudoCamera:
    def __init__(
        self,
        vid_path,
        s: socket.socket,
        images_dir,
        image_type,
        delay: int,
    ):
        self.vid_path = vid_path
        self.socket = s
        self.images_dir = images_dir
        self.image_type = image_type
        self.delay = delay

        if not os.path.exists(self.images_dir):
            os.mkdir(self.images_dir)
        
        self.cap = cv2.FileCapture(self.vid_path)
        time.sleep(2)
    
    def capture(self):
        timestamp = datetime.datetime.fromtimestamp(
            time.time()
        ).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        filename = f"{self.images_dir}/{timestamp}.{self.image_type}"
        ret, frame = self.cap.read()
        counts = 0
        while ret == False:
            counts += 1
            if counts > 5:
                self.cap.close()
                self.cap = cv2.FileCapture(self.vid_path)
            ret, frame = self.cap.read()
        cv2.imwrite(filename, frame)
        return filename


    def process(self):
        filename = self.capture()
        self.socket.send(cv2.imencode("." + self.image_type, cv2.imread(filename))[1].tobytes())
        time.sleep(self.delay)


def init_socket(server):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(server)
        print("Successfully created socket")
        return s
    except socket.error as err:
        print(f"Failed to create socket: {err}")
        sys.exit(1)


def main():
#    camera = Camera(RESOLUTION, init_socket(TARGET), IMAGES_DIR, IMAGE_TYPE, DELAY)
    camera = PseudoCamera(init_socket(TARGET), IMAGES_DIR, IMAGE_TYPE, DELAY)
    while True:
        camera.process()


if __name__ == "__main__":
    main()
