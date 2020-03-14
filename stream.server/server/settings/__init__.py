import os

DEBUG = True
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv('PORT', '5000'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.abspath(os.path.join(BASE_DIR, "pictures"))
APPLICATION_ROOT = ""
