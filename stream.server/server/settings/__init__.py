import os

DEBUG = True
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv('PORT', '5000'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLICATION_ROOT = ""
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "static"))
IMAGES_DIR = os.path.abspath(os.path.join(STATIC_ROOT, "pictures"))
