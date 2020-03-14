import socket

ip, port = "198.38.16.84", 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(1)
conn, addr = sock.accept()

print("Send data from pi")
data = conn.recv(1024)
print("Received: ", data.decode())
conn.close()
sock.close()
