import sys
from time import sleep
import socket as socketio
from picamera import PiCamera

MIDDLEMAN = ("localhost", 5000)  # (host, port)
DELAY = 5  # Interval to capture on


def init_camera():
    camera = PiCamera()
    camera.resolution(1024, 768)
    camera.start_preview()
    sleep(2)
    return camera


def init_socket():
    try:
        s = socketio.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(MIDDLEMAN)
        print("Successfully created socket")
        return s
    except socket.error as err:
        print(f"Failed to create socket: {err}")
        sys.exit(1)


def main():
    camera, socket = init_camera(), init_socket()
    while True:
        camera.capture(socket, "png")
        sleep(DELAY)


if __name__ == "__main__":
    main()
