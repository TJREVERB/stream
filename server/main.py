import socket
from flask import Flask
import threading
import sys

PORT = int(sys.argv[1])
file = open("log.txt", "w+")
file.write("Created\n")
file.write("Port" + PORT + "\n")
file.close()


def init_socket():
    ip, port = "198.38.16.84", 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1)
    conn, addr = sock.accept()
    return conn


def listen_socket(conn):
    BUFFER = 1024
    while True:
        data = conn.recv(BUFFER)
        ingest(data)


#conn = init_socket()
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'

app.run(PORT)
